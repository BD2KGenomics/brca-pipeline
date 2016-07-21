from matplotlib import pyplot as plt


BRCA1 = "/cluster/home/mollyzhang/brca-pipeline/resources/genome_sequences/brca1_hg38_no_flanking.txt"
BRCA2 = "/cluster/home/mollyzhang/brca-pipeline/resources/genome_sequences/brca2_hg38_no_flanking.txt"


def main():
    plot_score("BRCA1", "3")    


def plot_score(gene, direction):
    scores = []
    f = open("MES_data/{0}_{1}_score.txt".format(gene, direction), "r")
    for line in f:
        scores.append(float(line.strip().split("\t")[1]))
    plt.plot(scores)
    plt.show()


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
