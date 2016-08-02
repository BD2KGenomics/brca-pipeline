"""
compared the all possible SNP brca variants VCFSA result with the scraped data from the 
hci BRCA priors website and calculate consistency between the two
"""

from pprint import pprint as pp


MOLLY_RESULT = "/cluster/home/mollyzhang/splicing_variant/VCFSA_output/all_snp_brca_VCFSA.vcf"
HCI_WEBSITE = "/cluster/home/mollyzhang/brca-pipeline/splicing_prior/web_scraping/scraped_data/hci_priors_combined.txt"



def main():
    print len(get_Molly_result_as_dict())


def get_Molly_result_as_dict():
    result = {}
    f = open(MOLLY_RESULT, "r")
    for index, line in enumerate(f):
        if line.startswith("#") or "c.*" in line:
            continue
        info = line.strip().split("\t")[-1]
        HGVS = info.split(";")[0][5:]
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
                score = sj.split(",")[-1]
                scores[type] = score            
        result[HGVS] = scores
    return result


def extract_intron_position(HGVS):
    new_HGVS = HGVS.replace("c.-", "haha").replace("+", "-")
    if "-" not in new_HGVS:
        pos = 0
    else:
        pos = int(new_HGVS.split("-")[-1][:-3])
    return pos




if __name__ == "__main__":
    main()
