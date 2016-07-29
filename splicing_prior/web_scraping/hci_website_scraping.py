"""
download all html files containing VCFSplicingAnnotator scores
from http://priors.hci.utah.edu/PRIORS/index.php
"""


import urllib
from bs4 import BeautifulSoup
import sys 
import pprint

BASE_URL = "http://priors.hci.utah.edu/PRIORS/BRCA/"



def main():
    download()


def download():
    base_url = "http://priors.hci.utah.edu/PRIORS/BRCA/viewer.php?gene={0}&exon={1}"
    for gene in ["BRCA1", "BRCA2"]:
        soup = BeautifulSoup(urllib.urlopen(base_url.format(gene, "exon2")).read(), "html.parser")
        exon_tags = soup.findAll("td", {"class": "current-exon"}) + soup.findAll("td", {"class": 'exon'})
        for exon_tag in exon_tags:
            exon = exon_tag.a.contents[0]
            print "\n", gene, "exon{0}".format(exon)
            f_out = open("scraped_data/{0}_exon{1}.txt".format(gene, exon), "w")
            exon_url = base_url.format(gene, "exon" + exon)
            exon_soup = BeautifulSoup(urllib.urlopen(exon_url).read(), "html.parser")
            sequence = exon_soup.findAll("a", {"class": "seq"})
            for base in sequence:
                position = base.get('href').split("?")[1]
                for mutation in ["&mut=1", "&mut=2", "&mut=3"]:
                    create_line(f_out, position, mutation)
                break
            break
            f_out.close()
        break

def create_line(f, pos, mut):
    for splice_type in ["popdon?", "popwtacc?"]:
        this_url = BASE_URL + splice_type + pos + mut
        mut_soup = BeautifulSoup(urllib.urlopen(this_url).read(), "html.parser")
        hgvs = mut_soup.span.div.contents[0].encode("ascii", "replace").split("?")[-1]
        table_content = mut_soup.findAll("td")
        if splice_type == "popdon?":
            donor_score = table_content[13].div.contents[0]
        elif splice_type == "popwtacc?":
            acceptor_score = table_content[11].contents[0]
    line = "\t".join([hgvs, donor_score, acceptor_score]) + "\n"
    f.write(line)


if __name__ == "__main__":
    main()
