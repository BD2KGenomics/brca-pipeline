"""add VEP result to merged data"""
from pprint import pprint
import vcf
import pandas as pd

MERGED_FILE = "/cluster/home/mollyzhang/release1.0/merged.csv"
OUTPUT = "/cluster/home/mollyzhang/release1.0/merged_withVEP.csv"
VEP = "/cluster/home/mollyzhang/release1.0/data/VEP/vep_output_3_3_2016.vcf"
VEP_FIELDS = "Allele|Consequence|IMPACT|SYMBOL|Gene|Feature_type|Feature|BIOTYPE|EXON|INTRON|HGVSc|HGVSp|cDNA_position|CDS_position|Protein_position|Amino_acids|Codons|Existing_variation|DISTANCE|STRAND|SYMBOL_SOURCE|HGNC_ID|TSL|APPRIS|REFSEQ_MATCH|SIFT|PolyPhen|GMAF|AFR_MAF|AMR_MAF|EAS_MAF|EUR_MAF|SAS_MAF|AA_MAF|EA_MAF|ExAC_MAF|ExAC_Adj_MAF|ExAC_AFR_MAF|ExAC_AMR_MAF|ExAC_EAS_MAF|ExAC_FIN_MAF|ExAC_NFE_MAF|ExAC_OTH_MAF|ExAC_SAS_MAF|CLIN_SIG|SOMATIC|PHENO|PUBMED|MOTIF_NAME|MOTIF_POS|HIGH_INF_POS|MOTIF_SCORE_CHANGE"

def main():
    save_VEP_to_dict().values()

def save_VEP_to_dict():
    f = open(VEP, "r")
    vep_dict = {}
    for line in f:
        if "#" in line:
            continue

        items = line.replace(".", "-").strip().split("\t")
        genome_coor = "chr{0}:{1}:{2}>{3}".format(items[0],
                                                  items[1],
                                                  items[3],
                                                  items[4])
        if genome_coor not in vep_dict:
            if items[-1] != "-":
                vep_dict[genome_coor] = process_VEP_info(items[-1])
        else:
            raise Exception("bad time") 
    return vep_dict

def process_VEP_info(info):
    unwanted_fields = "Allele|SYMBOL|HGVSc|HGVSp|cDNA_position|CDS_position|Protein_position|DISTANCE|STRAND|SYMBOL_SOURCE|HGNC_ID|ExAC_MAF|ExAC_Adj_MAF|ExAC_AFR_MAF|ExAC_AMR_MAF|ExAC_EAS_MAF|ExAC_FIN_MAF|ExAC_NFE_MAF|ExAC_OTH_MAF|ExAC_SAS_MAF".split("|")

    infos = info[4:].split(",")
    row_list = []
    for each_info in infos:
        columns = VEP_FIELDS.split("|")
        values = each_info.split("|")
        result_dict = dict(zip(columns, values))
        for field in unwanted_fields:
            
        row_list. 

    df = pd.DataFrame(row_list)
    print df.head()
    return df 


if __name__ == "__main__":
    main()

