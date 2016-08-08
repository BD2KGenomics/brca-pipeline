"""
this scripts takes the enigma raw tsv file and process it to produce the format suitable for 
brcaexchange variant merging pipeline
"""

import glob
import numpy as np
import sys
import re
from pprint import pprint as pp
import pyhgvs
import pyhgvs.utils as pyhgvs_utils
from pygr.seqdb import SequenceFileDB
import hgvs.dataproviders.uta
import hgvs.parser
import hgvs.variantmapper



COLUMNS_TO_SAVE = np.array(["Gene_symbol", #Genomic_Coordinate
                            "Reference_sequence",
                            "HGVS", # change to HGVS_cDNA
                            "BIC_Nomenclature",
                            "Abbrev_AA_change",
                            "URL",
                            "Condition_ID_type",
                            "Condition_ID_value",
                            "Condition_category",
                            "Clinical_significance",
                            "Date_last_evaluated",
                            "Assertion_method",
                            "Assertion_method_citation",
                            "Clinical_significance_citations",
                            "Comment_on_clinical_significance",
                            "Collection_method",
                            "Allele_origin",
                            "ClinVarAccession"]) #"HGVS_protein"

OUTPUT_COLUMNS = [i + "_cDNA" if i == "HGVS" else i for i in COLUMNS_TO_SAVE] + ["HGVS_protein"]
OUTPUT_COLUMNS.insert(2, "Genomic_Coordinate")
GENOME = SequenceFileDB('/cluster/home/mollyzhang/reference_genome/hg38/hg38.fa')
HDP = hgvs.dataproviders.uta.connect()
EVM = hgvs.variantmapper.EasyVariantMapper(HDP,
    primary_assembly='GRCh37', alt_aln_method='splign')


def main():
    raw_files = glob.glob("raw_files/*batch1*tsv")
    f_out = open("output/ENIMGA_last_updated_05-21-2016.tsv", "w")
    f_out.write("\t".join(OUTPUT_COLUMNS) + "\n")
    f_in = open(raw_files[0], "r")
    for index, line in enumerate(f_in):
        if index in [0, 1, 3, 4]:
            continue
        items = np.array(line.rstrip().split("\t"))
        if index == 2:
            columns = np.array([i.replace(" ", "_") for i in items])
            index_to_save = [np.where(columns==i)[0][0] for i in COLUMNS_TO_SAVE]
            column_idx = dict(zip(COLUMNS_TO_SAVE, index_to_save))
            continue
        if len(items) != len(columns):
            continue
        OMIM_id_index = column_idx["Condition_ID_value"]
        items[OMIM_id_index] = convert_OMIM_id(items[OMIM_id_index])
        HGVS_cDNA = (items[column_idx["Reference_sequence"]] +
                     ":" + items[column_idx["HGVS"]])
        genome_coor = get_genome_coor(HGVS_cDNA)
        items = list(items[index_to_save])
        items.insert(2, genome_coor)
        HGVS_protein = HGVS_cDNA_to_protein(HGVS_cDNA) 
        items.append(HGVS_protein)
        new_line = "\t".join(list(items)) + "\n"
        f_out.write(new_line)
    f_in.close()
    f_out.close()


def convert_OMIM_id(OMIM_id):
    if OMIM_id == "604370":
        return "BREAST-OVARIAN CANCER, FAMILIAL, SUSCEPTIBILITY TO, 1; BROVCA1 (" + OMIM_id + ")" 
    elif OMIM_id == "612555":
        return "BREAST-OVARIAN CANCER, FAMILIAL, SUSCEPTIBILITY TO, 2; BROVCA2 (" + OMIM_id + ")" 
    else:
        raise Exception("OMIM id not found (" + OMIM_id + ")")


def get_genome_coor(hgvs_c):
    chrom, offset, ref, alt = pyhgvs.parse_hgvs_name(
        hgvs_c, GENOME, get_transcript=get_transcript)
    return chrom + ":" + str(offset) + ":" + ref + ">" + alt


def HGVS_cDNA_to_protein(hgvs_c):
    hp = hgvs.parser.Parser()
    hgvs_c = hp.parse_hgvs_variant(hgvs_c)
    hgvs_p = str(EVM.c_to_p(hgvs_c)).split(":")[1]
    return hgvs_p


def get_transcript(name):
    REFGENE = "../resources/refseq/hg38.BRCA.refGene.txt"
    with open(REFGENE) as infile:
        TRANSCRIPTS = pyhgvs_utils.read_transcripts(infile)
    return TRANSCRIPTS.get(name)


if __name__ == "__main__":
    main()
