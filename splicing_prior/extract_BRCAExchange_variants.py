import fileinput
import os
import pdb
import argparse

import hgvs_conversion as hc



FILE = "/hive/groups/cgl/brca/release1.0/pipeline_output/merged_15Jul2016.csv"
SNP_VCF = "VCFSA_data/brcaExchange_SNPs.vcf"
INDEL_VCF="VCFSA_data/brcaExchange_INDELs.vcf"
OTHER="VCFSA_data/brcaExchange_others.txt"


parser = argparse.ArgumentParser(description="seperate brca exchange data to snps and indels")
parser.add_argument("input", help="input file")
args = parser.parse_args()




def main():
    write_header()
    f = open(args.input, "r")
    f_snp = open(SNP_VCF + ".body", "w")
    f_indel = open(INDEL_VCF + ".body", "w")    
    f_other = open(OTHER, "w")
    n_snp = 0
    n_indel = 0
    n_other = 0
    for index, line in enumerate(f):
        if index == 0:
            continue
        items = line.strip().split(",")
        genome_coor = items[2]
        if "|" in genome_coor:
            genome_coor = genome_coor.split("|")[0]
        chr, pos, refalt = genome_coor.replace("-", "").split(":")
        ref, alt = refalt.split(">")
        if items[3] == "-":
            if ref == "None" or alt == "None" or ref == alt or (len(ref) == len(alt) and len(ref) > 1):  
                HGVS = "."
            else: HGVS = hc.VCF_to_HGVS([chr, int(pos), ref, alt])
        else:
            HGVS = items[3] + ":" + items[4]
        info = "{0}".format(HGVS)
        if ref == "":
            ref = "-"
        if alt == "":
            alt = "-"
        new_line = "\t".join([chr[-2:], str(pos), ".", ref, alt, ".", ".", info]) + "\n"
        if ref == "None" or alt == "None":
            n_other += 1
            f_other.write(line)
        elif len(ref) == len(alt):
            if ref == alt:
                n_other += 1
                f_other.write(line)
            else:
                if len(ref) == 1:    
                    n_snp += 1
                    f_snp.write(new_line)
                else:
                    n_other += 1
                    f_other.write(line)
        else:
            n_indel += 1
            f_indel.write(new_line)    
    f.close()
    f_snp.close()
    f_indel.close()
    f_other.close()
    for filename in [SNP_VCF, INDEL_VCF]:
        with open(filename, "w") as file:
            file_list = ["VCFSA_data/vcf_header.txt", filename + ".body"]
            input_lines = fileinput.input(file_list)
            file.writelines(input_lines)
            file.close()
        os.remove(filename + ".body")
    print "number of SNPs: ", n_snp
    print "number of indels: ", n_indel
    print "number of unprocessed cases: ", n_other

def write_header(version="GRCh38"):
    with open('VCFSA_data/vcf_header.txt', 'w') as f_header:
        f_header.write("##fileformat=VCFv4.0\n")
        f_header.write("##reference={0}\n".format(version))
        f_header.write("##INFO=<ID=HGVS,Number=.,Type=String,Description=\"HGVS representation of this variant\">\n")
        f_header.write("\t".join(
            ["#CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO\n"]))
        f_header.close()


if __name__ == "__main__":
    main()
