"""
1. generate all BRCA SNPs
2. generate BRCA deletion variants up to size 10bp
3. generate BRCA insertion variants up to size 3bp
"""

import fileinput
import os


BRCA2 = {"start": 32889617,
         "seq": open("../resources/brca2_hg19_no_flanking.txt", "r").read().upper()}
BRCA1 = {"start": 41196312,
         "seq": open("../resources/brca1_hg19_no_flanking.txt", "r").read().upper()}
SNP_VCF = "all_snp_brca.vcf"
INSERT_VCF = "insertion_brca.vcf"
DELETE_VCF = "deletion_brca.vcf"




def main():
    create_SNP_vcf()    


def create_SNP_vcf():
    write_header()
    f_out = open(SNP_VCF + ".body", "w")
    for gene, BRCA in {'brca1': BRCA1, 'brca2': BRCA2}.iteritems():
        for i in range(len(BRCA['seq'])):
            if gene == 'brca1':
                chr = '17'
            elif gene == 'brca2':
                chr = '13'
            else:
                raise Exception('bad time')
            pos = i + BRCA['start'] + 1
            ref = BRCA['seq'][i]
            alts = 'AGTC'.replace(ref, '')
            check_ref_correct([chr, pos, ref, alts[0]])
            for alt in alts:
                info = 'Dummy=dummy'
                new_line = "\t".join([chr, str(pos), ".", ref, alt, ".", ".", info])
                f_out.write(new_line + "\n")
    f_out.close()
    
    # merge header and body
    with open(SNP_VCF, "w") as file:
        file_list = ["vcf_header.txt", SNP_VCF + ".body"]
        input_lines = fileinput.input(file_list)
        file.writelines(input_lines)
    for each_file in file_list:
        os.remove(each_file)


def write_header():
    with open('vcf_header.txt', 'w') as f:
        f.write("##fileformat=VCFv4.0\n")
        f.write("##reference=GRCh37\n")
        f.write("##INFO=<ID=Dummy,Number=.,Type=String,Description=\"\">\n")
        f.write("\t".join(
            ["#CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO\n"]))
        f.close()

def check_ref_correct(v):
    chr, pos, ref, alt = v
    pos = int(pos)
    if chr == "13":
        seq = BRCA2['seq']
        pos = pos - 1 - BRCA2['start']
    elif chr == "17":
        seq = BRCA1['seq']
        pos = pos - 1 - BRCA1['start']
    else:
        assert(False)

    genomeRef = seq[pos:pos+len(ref)].upper()
    if len(ref) != 0 and len(genomeRef)==0:
        print chr, pos, ref, alt
        raise Exception("ref not inside BRCA1 or BRCA2")
    assert(genomeRef == ref)



if __name__=="__main__":
    main()
