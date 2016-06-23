"""
generate all BRCA SNPs
"""

BRCA2 = {"start": 32889617,
         "seq": open("../resources/brca2_hg19_no_flanking.txt", "r").read().upper()}
BRCA1 = {"start": 41196312,
         "seq": open("../resources/brca1_hg19_no_flanking.txt", "r").read().upper()}
VCF_FILE = "all_snp_brca.vcf"



def main():
    create_vcf()    



def create_vcf():
    f_out = open(VCF_FILE, "w")
    f_out.write("##fileformat=VCFv4.0\n")
    f_out.write("##reference=GRCh37\n")
    f_out.write("##INFO=<ID=,Number=.,Type=String,Description=\"\">\n")
    f_out.write("\t".join(
        ["#CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO\n"]))
    
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
                new_line = "\t".join([chr, str(pos), ".", ref, alt, ".", ".", "."])
                f_out.write(new_line + "\n")
    f_out.close()

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
