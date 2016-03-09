import pandas as pd
import ast
import pandas_profiling




def main():
    step1("raw_data/merged_withVEP_cleaned.csv", "raw_data/BRCA_data_step1.csv")
    step2("raw_data/BRCA_data_step1.csv", "raw_data/BRCA_data_step2.csv")
    step3("raw_data/BRCA_data_step2.csv", "raw_data/BRCA_data_step3.csv")
    step4("raw_data/BRCA_data_step3.csv", "raw_data/BRCA_data_step4.csv")

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
                          "Literature_source(exLOVD)", "Method(ClinVar)"
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