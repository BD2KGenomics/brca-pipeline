import pysam

chr13_fa = "/cluster/home/mollyzhang/reference_genome/hg38/chr13.fa"
chr17_fa = "/cluster/home/mollyzhang/reference_genome/hg38/chr17.fa"
BRCA1_NO_FLANK = "brca1_hg38_no_flanking.txt"
BRCA2_NO_FLANK = "brca2_hg38_no_flanking.txt"


def main():
    fetch()


def fetch():
    chr13 = pysam.FastaFile(chr13_fa)
    chr17 = pysam.FastaFile(chr17_fa)
    BRCA2 = chr13.fetch(reference="chr13", start=32315474, end=32400266)
    BRCA1 = chr17.fetch(reference="chr17", start=43045629, end=43125483)
    
    open(BRCA1_NO_FLANK, "w").write(BRCA1)
    open(BRCA2_NO_FLANK, "w").write(BRCA2)

if __name__=="__main__":
    main()

