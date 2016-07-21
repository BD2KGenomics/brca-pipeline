BRCA1 = "/cluster/home/mollyzhang/brca-pipeline/resources/genome_sequences/brca1_hg38_no_flanking.txt"
BRCA2 = "/cluster/home/mollyzhang/brca-pipeline/resources/genome_sequences/brca2_hg38_no_flanking.txt"


def main():
    get_MES_inputfile("BRCA1", "3")    
    get_MES_inputfile("BRCA2", "3")    
    get_MES_inputfile("BRCA1", "5")    
    get_MES_inputfile("BRCA2", "5")    


def get_MES_inputfile(gene, direction):
    if gene == "BRCA1":
        sequence = open(BRCA1, "r").read()
    elif gene == "BRCA2":
        sequence = open(BRCA2, "r").read()
    else:
        assert(False)

    if direction == "3":
        window = 23
    elif direction == "5":
        window = 9
    else:
        assert(False)

    f_out = open("MES_data/{0}_{1}.txt".format(gene, direction), "w")
    for i in range(len(sequence) - window + 1):
        f_out.write(sequence[i: i+window] + "\n")
    f_out.close()




if __name__ == "__main__":
    main()
