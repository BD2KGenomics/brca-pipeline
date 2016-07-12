import pysam

chr13_fa = "/cluster/home/mollyzhang/reference_genome/hg19/chr13.fa"
chr17_fa = "/cluster/home/mollyzhang/reference_genome/hg19/chr17.fa"
BRCA1_START = 41196312
BRCA2_START = 32889617
BRCA1_FLANK = open("brca1_hg19.txt", "r").read() 
BRCA2_FLANK = open("brca2_hg19.txt", "r").read() 
BRCA1_NO_FLANK = open("brca1_hg19_no_flanking.txt", "r").read() 
BRCA2_NO_FLANK = open("brca2_hg19_no_flanking.txt", "r").read() 


def main():
    check_correct()



def check_correct():
    testfile = open("ENIGMA_GRCh37_test.txt", "r")
    line_num = 1 
    outside_num = 0
    for line in testfile:
        line_num += 1
        line.replace("-", "")
        chr, pos, refalt = line.strip().split(":")
        pos = int(pos)
        ref, alt = refalt.split(">")
        chr = chr[-2:]
        if chr == "13":
            seq = BRCA2_NO_FLANK
            pos = pos - 1 - BRCA2_START
        elif chr == "17":
            seq = BRCA1_NO_FLANK
            pos = pos - 1 - BRCA1_START
        else:
            assert(False)

        if pos < 0 or pos > len(seq):
            outside_num += 1
            continue
        genomeRef = seq[pos:pos+len(ref)].upper()
        if len(ref) != 0 and len(genomeRef)==0:
            print chr, pos, ref, alt
            raise Exception("ref not inside BRCA1 or BRCA2")
        assert(genomeRef == ref)


    print "number of variants outside BRCA1, BRCA2 CDS: ", outside_num


def fetch():
    chr13 = pysam.FastaFile(chr13_fa)
    chr17 = pysam.FastaFile(chr17_fa)
    BRCA2 = chr13.fetch(reference="chr13", start=32889617, end=32973809)
    BRCA1 = chr17.fetch(reference="chr17", start=41196312, end=41277500)
    
    open(brca1, "w").write(BRCA1)
    open(brca2, "w").write(BRCA2)

if __name__=="__main__":
    main()

