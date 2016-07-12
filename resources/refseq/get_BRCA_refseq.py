HG19 = "hg19.refGene.txt"
HG38 = "hg38.refGene.txt"
BRCA1 = "NM_007294"
BRCA2 = "NM_000059"



f19 = open(HG19, "r")
f19_out = open("hg19.BRCA.refGene.txt", "w")

f38 = open(HG38, "r")
f38_out = open("hg38.BRCA.refGene.txt", "w")




for line in f19:
    gene_id = line.strip().split("\t")[1].split(".")[0]
    if gene_id == BRCA1 or gene_id == BRCA2:
        f19_out.write(line)

f19.close()
f19_out.close()


for line in f38:
    gene_id = line.strip().split("\t")[1].split(".")[0]
    if gene_id == BRCA1 or gene_id == BRCA2:
        f38_out.write(line)

f38.close()
f38_out.close()
