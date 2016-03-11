import pysam
chr13_fa = "/cluster/home/mollyzhang/chr13.fa"
chr17_fa = "/cluster/home/mollyzhang/chr17.fa"
brca1 = "/cluster/home/mollyzhang/brca_repo/resources/brca1_hg38.txt"
brca2 = "/cluster/home/mollyzhang/brca_repo/resources/brca2_hg38.txt"


chr13 = pysam.FastaFile(chr13_fa)
chr17 = pysam.FastaFile(chr17_fa)
BRCA2 = chr13.fetch(reference="chr13", start=32300000, end=32500000)
BRCA1 = chr17.fetch(reference="chr17", start=43000000, end=43200000)

open(brca1, "w").write(BRCA1)
open(brca2, "w").write(BRCA2)



