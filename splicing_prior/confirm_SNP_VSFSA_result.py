"""
compared the all possible SNP brca variants VCFSA result with the scraped data from the 
hci BRCA priors website and calculate consistency between the two
"""

from pprint import pprint as pp


MOLLY_RESULT = "/cluster/home/mollyzhang/splicing_variant/VCFSA_output/all_snp_brca_VCFSA.vcf"
HCI_WEBSITE = "/cluster/home/mollyzhang/brca-pipeline/splicing_prior/web_scraping/scraped_data/hci_priors_combined.txt"



def main():
    molly_result = get_Molly_result_as_dict()
    compare_results(molly_result, HCI_WEBSITE)    


def compare_results(result1, filename):
    overlap = 0
    donor_match = 0
    f = open(filename, "r")
    for index, line in enumerate(f):
        if index == 0:
            continue
        if index %1000 == 0:
            print index
        items = line.strip().split("\t")
        HGVS = "({0}):{1}".format(items[3], items[0].strip()).upper()
        if HGVS in result1:
            overlap += 1
            donor = items[1]
            print HGVS
            print donor
            print result1[HGVS]
            if donor == result1[HGVS]["donor"]:
                donor_match += 1 

    percent_overlap = (overlap/(float(index) + 1)) * 100
    print "%.2f percent hci website results can be found in Molly's result" %(percent_overlap)
    print donor_match


def get_Molly_result_as_dict():
    print "save Molly's result to dictionary....."
    result = {}
    f = open(MOLLY_RESULT, "r")
    for index, line in enumerate(f):
        if line.startswith("#") or "c.*" in line:
            continue
        info = line.strip().split("\t")[-1]
        HGVS = "(" + info.split(";")[0][5:].split("(")[-1].upper()
        position = extract_intron_position(HGVS)
        if position >= 26:
            continue
        if "VCFSA" not in info:
            scores = {"3": "NA", "5": "NA"}
        else:
            MES = info.split("VCFSA=")[-1]
            scores = {}
            for sj in MES.split(":"):
                type = sj.split(",")[0][1]
                if type == "3":
                    type = "acceptor"
                elif type == "5":
                    type = "donor"
                else:
                    raise Exception("bad time")
                score = sj.split(",")[-1]
                scores[type] = score
        result[HGVS] = scores
    return result


def extract_intron_position(HGVS):
    new_HGVS = HGVS.replace("C.-", "haha").replace("+", "-")
    if "-" not in new_HGVS:
        pos = 0
    else:
        pos = int(new_HGVS.split("-")[-1][:-3])
    return pos




if __name__ == "__main__":
    main()
