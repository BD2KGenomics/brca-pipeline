import pandas as pd
import ast

def main():
    #step1()
    #step2()
    step3()

def step3():


    z = ast.literal_eval("[0.1,0.2]")
    print type(z)




def step2():
    """remove unwanted columns/features"""
    to_remove = ["BIC_Nomenclature(ENIGMA)", "Abbrev_AA_change(ENIGMA)", "URL(ENIGMA)",
                 "Condition_ID_type(ENIGMA)", "Condition_ID_value(ENIGMA)", "Condition_category(ENIGMA)",
                 "Date_last_evaluated(ENIGMA)", "ClinVarAccession(ENIGMA)", "Date_Last_Updated(ClinVar)",
                 "SCV(ClinVar)", "BIC_identifier(exLOVD)", "Allele(VEP)", "SYMBOL(VEP)", "Gene(VEP)",
                 "Feature_type(VEP)", "Feature(VEP)", "HGVSc(VEP)", "HGVSp(VEP)", "cDNA_position(VEP)",
                 "CDS_position(VEP)", "Protein_position(VEP)", "SYMBOL_SOURCE(VEP)", "HGNC_ID(VEP)"]
    df=pd.read_csv("data/BRCA_data_preprocessed.csv")
    for each_column in to_remove:
        df.drop(each_column, axis=1, inplace=True)

    df.to_csv("data/BRCA_data_preprocessed1.csv")


def step1():
    """
    1. rename VEP columns from style as "VEP_column_name" to column_name(VEP), so it's consistent across all columns
    2. replace a cell of value "-" with empty string
    """
    f = open("data/merged_withVEP.csv", "r")
    f_out = open("data/BRCA_data_preprocessed.csv", "w")
    line_num = 0
    for line in f:
        line_num +=1
        # fix VEP column name
        if line_num == 1:
            columns = line.strip().split(",")
            new_columns = []
            for column in columns:
                if "VEP" in column:
                    column = column[4:] + "(VEP)"
                new_columns.append(column)
            new_line = ",".join(new_columns) + "\n"
            print new_line
        else:
            # replace "-" with empty string
            cells = line.strip().split(",")
            new_cells = []
            for cell in cells:
                if cell == "-":
                    cell = ""
                new_cells.append(cell)
            new_line = ",".join(new_cells) + "\n"
        f_out.write(new_line)


if __name__ == '__main__':
    main()