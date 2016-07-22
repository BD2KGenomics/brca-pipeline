"""
Note: these things are the same:
3' of an intron == splice acceptor == 23nt sequence
5' of an intron == splice donor == 9nt sequence 
"""

from matplotlib import pyplot as plt
import numpy as np
from pprint import pprint as pp
import subprocess


BRCA1 = "../resources/genome_sequences/brca1_hg38_no_flanking.txt"
BRCA2 = "../resources/genome_sequences/brca2_hg38_no_flanking.txt"
REFSEQ = "../resources/refseq/hg38.BRCA.refGene.txt"
MES_CUTOFF = 6  # MES scores lower than MES_cutoff won't be plotted

def main():
    #create_MES_inputfile()
    #run_MaxEntScan()
    plot_score("BRCA1")

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


def plot_score(gene):
    gene_strand = {"BRCA1": "-", "BRCA2": "+"}
    scores = get_MES_score(gene)
    scores = scores[gene_strand[gene]]
    plt.plot(scores["donor"])
    plt.plot(scores["acceptor"])
    plt.title(gene)
    plt.legend(["donor", "acceptor"])
    plt.show()


def get_MES_score(gene):
    scores = {"+": {"donor": [], "acceptor": []},
              "-": {"donor": [], "acceptor": []}}
    for strand in scores.keys():
        for sj in scores[strand].keys():
            f = open("MES_data/score_{0}_{1}_{2}.txt".format(gene, sj, strand), "r")
            for line in f:
                scores[strand][sj].append(float(line.strip().split("\t")[1]))
            scores[strand][sj] = np.array(scores[strand][sj])
            scores[strand][sj][scores[strand][sj] <= MES_CUTOFF] = MES_CUTOFF
    return scores


def create_MES_inputfile():
    """
    8 files: BRCA1/BRCA2, postive/negative strand, splice donor/acceptor
    """
    files = {"BRCA1": BRCA1, "BRCA2": BRCA2}
    sj_dict = {"donor": 9, "acceptor": 23}
    sequence = {"+": "", "-": ""}
    for gene in ["BRCA1", "BRCA2"]:
        sequence["+"] = open(files[gene], "r").read().upper().strip()
        sequence["-"] = reverse_complement(sequence["+"])
        for strand in ["+", "-"]:
            for sj, window in sj_dict.iteritems():
                f_out = open("MES_data/{0}_{1}_{2}.txt".format(gene, sj, strand), "w")
                for i in range(len(sequence[strand]) - window + 1):
                    f_out.write(sequence[strand][i: i+window] + "\n")
                f_out.close()


def run_MaxEntScan(): 
    """" 
    run MaxEntScan by calling perl script via subprocess module 
    """ 
    MES_dict = {"acceptor": "MaxEntScan/score3.pl", "donor": "MaxEntScan/score5.pl"} 
    for gene in ["BRCA1", "BRCA2"]: 
        for strand in ["+", "-"]: 
            for sj, MES in MES_dict.iteritems(): 
                inputfile = "MES_data/{0}_{1}_{2}.txt".format(gene, sj, strand)      
                f_out = open("MES_data/score_{0}_{1}_{2}.txt".format(gene, sj, strand), "w")   
                subprocess.call(["perl", MES, inputfile], stdout=f_out) 
                f_out.close() 
    return "Done" 


def reverse_complement(sequence):
    complement = {"A":"T", "T":"A", "G":"C", "C":"G"}
    return "".join([complement[each] for each in sequence[::-1]])


if __name__ == "__main__":
    main()
