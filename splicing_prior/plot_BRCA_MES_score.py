from matplotlib import pyplot as plt
import numpy as np
from pprint import pprint as pp


BRCA1 = "/cluster/home/mollyzhang/brca-pipeline/resources/genome_sequences/brca1_hg38_no_flanking.txt"
BRCA2 = "/cluster/home/mollyzhang/brca-pipeline/resources/genome_sequences/brca2_hg38_no_flanking.txt"
REFSEQ = "/Users/Molly/Desktop/Genomics Research/brca-pipeline/resources/refseq/hg38.BRCA.refGene.txt"


def main():
    #plot_score("BRCA1", "3")    
    print get_exon_boundaries("BRCA1")

def get_exon_boundaries(gene):
    """
    return splicing donor (5' end of intron) sites
     and splicing acceptor (3' end of intron) list as two lists
    """
    brca2_refseq, brca1_refseq, dummy = open(REFSEQ, "r").read().split("\n")
    refseq = {"BRCA1": brca1_refseq.split("\t"),
              "BRCA2": brca2_refseq.split("\t")}
    exon_starts = refseq[gene][9][:-1].split(",") # splicing acceptors
    exon_ends = refseq[gene][10][:-1].split(",") # splicing donors
    return exon_starts, exon_ends


def plot_score(gene, direction):
    scores = []
    f = open("MES_data/{0}_{1}_score.txt".format(gene, direction), "r")
    for line in f:
        scores.append(float(line.strip().split("\t")[1]))
    
    scores = np.array(scores)
    scores[scores<=6] = 6
    plt.plot(scores)
    plt.title("BRCA1")
    plt.legend(["3 prime", "5 prime"])
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
