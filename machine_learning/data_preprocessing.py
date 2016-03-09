import pandas as pd
import ast
import pandas_profiling
import numpy as np
from matplotlib import pyplot as plt



def main():
    # step1("raw_data/merged_withVEP_cleaned.csv", "raw_data/BRCA_data_step1.csv")
    # step2("raw_data/BRCA_data_step1.csv", "raw_data/BRCA_data_step2.csv")
    # step3("raw_data/BRCA_data_step2.csv", "raw_data/BRCA_data_step3.csv")
    # step4("raw_data/BRCA_data_step3.csv", "raw_data/BRCA_data_step4.csv")
    # step5("raw_data/BRCA_data_step4.csv", "raw_data/BRCA_data_step5.csv")
    # step6("raw_data/BRCA_data_step5.csv", "raw_data/BRCA_data_with_label")
    step7("raw_data/BRCA_data_with_label", "raw_data/BRCA_data_with_label_1")
    step8("raw_data/BRCA_data_with_label_1", "raw_data/BRCA_data_with_label_2")






def step7(input, output):
    """
    remove fields in which more than 80% of the value is missing
    """
    df = pd.read_csv(input)
    record_num = len(df)
    for column in df.columns:
        nan_num = record_num - df[column].count()
        if nan_num/float(record_num) > 0.8:
            df.drop(column, axis=1, inplace=True)
    df.to_csv(output, index=None)


def step8(input, output):
    """parse submitter names to consistent ones"""
    submitters = []
    df = pd.read_csv(input)
    for index, row in df.iterrows():
        submitter = row["Submitter(ClinVar)"]
        if "|" in submitter:
            submitters.append("Multiple")
        else:
            if "ENIGMA" in submitter:
                submitters.append("ENGIMA")
            elif "BIC" in submitter:
                submitters.append("BIC")
            elif "SCRP" in submitter:
                submitters.append("SCRP")
            else:
                submitters.append(submitter)
    df["Submitters"] = submitters
    df.drop("Submitter(ClinVar)", axis=1, inplace=True)
    df.to_csv(output, index=False)





def step6(input, output):
    """
    sepearte out the part of data that have labels
    """
    df = pd.read_csv(input)
    with_label_rows = []
    for index, row in df.iterrows():
        if not pd.isnull(row["labels"]):
            with_label_rows.append(row)
    labeled_df = pd.DataFrame(with_label_rows)
    labeled_df.to_csv(output, index=None)



def step5(input, output):
    """add label based on the field "Clinical_Significance(ClinVar)"
    """
    df = pd.read_csv(input)
    labels = []
    for index, row in df.iterrows():
        clin_sig = row['Clinical_Significance(ClinVar)']
        if pd.isnull(clin_sig):
            labels.append("")
        else:
            clin_sig = clin_sig.lower()
            if "unknown" in clin_sig or "uncertain" in clin_sig:
                labels.append("")
            else:
                if "benign" in clin_sig and "patho" in clin_sig:
                    labels.append("")
                elif "benign" in clin_sig and "patho" not in clin_sig:
                    labels.append("benign")
                elif "benign" not in clin_sig and "patho" in clin_sig:
                    labels.append("pathogenic")
                else:
                    labels.append("")
    df['labels'] = labels
    df.drop("Clinical_Significance(ClinVar)", axis=1, inplace=True)
    df.to_csv(output, index=None)



def step4(input, output):
    """merge allele frequency from 1000 genome and exac
    replace "-", "?" with nan in various fields
    """
    df=pd.read_csv(input)
    afs = []
    for index, row in df.iterrows():
        onekg = row["Allele_frequency(1000_Genomes)"]
        exac = row["Allele_frequency(ExAC)"]
        af = 0
        if pd.isnull(onekg) and not pd.isnull(exac):
            af = exac
        if not pd.isnull(onekg) and pd.isnull(exac):
            af = onekg
        if not pd.isnull(onekg) and not pd.isnull(exac):
            af = (onekg + exac)/2
        if af == 0:
            af = ""
        afs.append(af)
        for column in row.keys():
            if (row[column] == "-" or row[column] == "?" or
                    (type(row[column]) == str and row[column].lower() == "unknown")):
                df.set_value(index, column, "")

    df["Allele_frequency(1000g_exac)"] = afs
    df.drop("Allele_frequency(1000_Genomes)", axis=1, inplace=True)
    df.drop("Allele_frequency(ExAC)", axis=1, inplace=True)
    df.to_csv(output, index=None)


def step2(input, output):
    """extract cases like [0.0]"""
    df=pd.read_csv(input)
    for index, row in df.iterrows():
        for key, value in row.iteritems():
            if type(value) == str and value[0] == "[" and value[-1] == "]":
                df.set_value(index, key, ast.literal_eval(value)[0])
    df.to_csv(output, index=None)


def step3(input, output):
    """remove unwanted columns/features"""
    meaningless_fields = ["BIC_Nomenclature(ENIGMA)", "Abbrev_AA_change(ENIGMA)",
                          "URL(ENIGMA)", "Condition_ID_type(ENIGMA)",
                          "Condition_ID_value(ENIGMA)", 'Condition_category(ENIGMA)',
                          "Date_last_evaluated(ENIGMA)", 'ClinVarAccession(ENIGMA)',
                          'HGVS_protein(ENIGMA)', 'Date_Last_Updated(ClinVar)',
                          "PUBMED(VEP)", 'HGVS(ClinVar)','SCV(ClinVar)',
                          'BIC_identifier(exLOVD)', "Clinical_classification(BIC)",
                          "Clinical_importance(BIC)", "Clinical_significance(ENIGMA)",
                          "Existing_variation(VEP)", "Germline_or_Somatic(BIC)",
                          "HGVS_cDNA(ENIGMA)", "Source", "Allele_origin(ENIGMA)",
                          "BIC_Designation(BIC)", "Reference_sequence(ENIGMA)",
                          "Clinical_significance_citations(ENIGMA)",
                          "Literature_source(exLOVD)", "Method(ClinVar)",
                          "Amino_acids(VEP)", "Codons(VEP)", "DISTANCE(VEP)",
                          "Literature_citation(BIC)"
                          ]

    redudant_fields = ["SAS_Allele_frequency(1000_Genomes)",
                       "AMR_Allele_frequency(1000_Genomes)",
                       "AFR_Allele_frequency(1000_Genomes)",
                       "EAS_Allele_frequency(1000_Genomes)",
                       "EUR_Allele_frequency(1000_Genomes)",
                       "Gene_symbol(ENIGMA)"
                       ]

    constant_fields = ["HIGH_INF_POS(VEP)", "MOTIF_NAME(VEP)",
                       "MOTIF_SCORE_CHANGE(VEP)", "MOTIF_POS(VEP)",
                       "APPRIS(VEP)",
                       "Allele_Origin(ClinVar)", "Assertion_method(ENIGMA)",
                       "Assertion_method_citation(ENIGMA)", "BIOTYPE(VEP)",
                       "Collection_method(ENIGMA)", "REFSEQ_MATCH(VEP)"]
    df=pd.read_csv(input)
    for each_column in meaningless_fields + redudant_fields + constant_fields:
        df.drop(each_column, axis=1, inplace=True)

    df.to_csv(output, index=None)


def step1(input, output):
    """
    replace a cell of value "-" with empty string
    """
    f = open(input, "r")
    f_out = open(output, "w")
    for line in f:
        cells = line.strip().split(",")
        new_cells = []
        for cell in cells:
            if cell == "-" or cell.upper()=="UNKNOWN":
                cell = ""
            new_cells.append(cell)
        new_line = ",".join(new_cells) + "\n"
        f_out.write(new_line)


if __name__ == '__main__':
    main()