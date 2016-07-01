FILE = "/hive/groups/cgl/brca/release1.0/pipeline_output/merged_01Jul2016.csv"


def main():
    f = open(FILE, "r")
    n_snp = 0
    n_indel = 0
    for index, line in enumerate(f):
        if index == 0:
            continue
        items = line.strip().split(",")
        genome_coor = items[2]
        if "|" in genome_coor:
            genome_coor = genome_coor.split("|")[0]
        ref, alt = genome_coor.replace("-", "").split(":")[2].split(">")
        if len(ref) == len(alt):
            n_snp += 1
        else:
            n_indel += 1
    print n_snp
    print n_indel




if __name__ == "__main__":
    main()
