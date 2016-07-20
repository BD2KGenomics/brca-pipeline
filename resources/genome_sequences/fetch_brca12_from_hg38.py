import pysam

chr13_fa = "/cluster/home/mollyzhang/reference_genome/hg38/chr13.fa"
chr17_fa = "/cluster/home/mollyzhang/reference_genome/hg38/chr17.fa"
BRCA1_START = 41196312
BRCA2_START = 32889617
BRCA1_FLANK = open("brca1_hg38.txt", "r").read() 
BRCA2_FLANK = open("brca2_hg38.txt", "r").read() 
BRCA1_NO_FLANK = open("brca1_hg38_no_flanking.txt", "r").read() 
BRCA2_NO_FLANK = open("brca2_hg38_no_flanking.txt", "r").read() 


def main():
    fetch()


def fetch():
    chr13 = pysam.FastaFile(chr13_fa)
    chr17 = pysam.FastaFile(chr17_fa)
    BRCA2 = chr13.fetch(reference="chr13", start=32889617, end=32973809)
    BRCA1 = chr17.fetch(reference="chr17", start=41196312, end=41277500)
    
    open(brca1, "w").write(BRCA1)
    open(brca2, "w").write(BRCA2)

if __name__=="__main__":
    main()

