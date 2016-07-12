import fileinput
import os
import pdb

import generate_BRCA_variant as gbv


FILE = "/hive/groups/cgl/brca/release1.0/pipeline_output/merged_01Jul2016.csv"
SNP_VCF = "VCFSA_data/brcaExchange_SNPs.vcf"
INDEL_VCF="VCFSA_data/brcaExchange_INDELs.vcf"


def main():
    gbv.write_header()
    f = open(FILE, "r")
    f_snp = open(SNP_VCF + ".body", "w")
    f_indel = open(INDEL_VCF + ".body", "w")    
    n_snp = 0
    n_indel = 0
    for index, line in enumerate(f):
        if index == 0:
            continue
        items = line.strip().split(",")
        genome_coor = items[2]
        if "|" in genome_coor:
            genome_coor = genome_coor.split("|")[0]
        chr, pos, refalt = genome_coor.replace("-", "").split(":")
        ref, alt = refalt.split(">")
        chr = chr[-2:]
        info = "Dummy=dummy"
        if ref == "":
            ref = "-"
        if alt == "":
            alt = "-"
        new_line = "\t".join([chr, str(pos), ".", ref, alt, ".", ".", info]) + "\n"
        if len(ref) == len(alt):
            n_snp += 1
            f_snp.write(new_line)
        
        else:
            n_indel += 1
            f_indel.write(new_line)
    f.close()
    f_snp.close()
    f_indel.close()
    for filename in [SNP_VCF, INDEL_VCF]:
        with open(filename, "w") as file:
            file_list = ["VCFSA_data/vcf_header.txt", filename + ".body"]
            input_lines = fileinput.input(file_list)
            file.writelines(input_lines)
            file.close()
        os.remove(filename + ".body")
    print "number of SNPs: ", n_snp
    print "number of indels: ", n_indel


def write_header(version="GRCh38"):
    with open('vcf_header.txt', 'w') as f_header:
        f_header.write("##fileformat=VCFv4.0\n")
        f_header.write("##reference={0}\n".format(version))
        f_header.write("##INFO=<ID=Dummy,Number=.,Type=String,Description=\"\">\n")
        f_header.write("\t".join(
            ["#CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO\n"]))
        f_header.close()


if __name__ == "__main__":
    main()
