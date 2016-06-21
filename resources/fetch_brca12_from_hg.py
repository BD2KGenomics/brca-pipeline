import pysam
chr13_fa = "/cluster/home/mollyzhang/reference_genome/hg19/chr13.fa"
chr17_fa = "/cluster/home/mollyzhang/reference_genome/hg19/chr17.fa"
brca1 = "/cluster/home/mollyzhang/brca_repo/resources/brca1_hg19_no_flanking.txt"
brca2 = "/cluster/home/mollyzhang/brca-pipeline/resources/brca2_hg19_no_flanking.txt"

chr13 = pysam.FastaFile(chr13_fa)
chr17 = pysam.FastaFile(chr17_fa)
BRCA2 = chr13.fetch(reference="chr13", start=32889617, end=32973809)
BRCA1 = chr17.fetch(reference="chr17", start=41196312, end=41277500)

open(brca1, "w").write(BRCA1)
open(brca2, "w").write(BRCA2)



