"""
download all html files containing VCFSplicingAnnotator scores
from http://priors.hci.utah.edu/PRIORS/index.php
"""


import urllib
from bs4 import BeautifulSoup
import sys 

BASE_URL = "http://priors.hci.utah.edu/PRIORS/BRCA/"
URL_PREFIX = {"donor": BASE_URL + "popdon.php?", 
              "acceptor": BASE_URL + "popwtacc.php?"}


def main():
    build_table() 


def build_table():

    # acceptor
    example = "html_data/popwtacc.php?gene=BRCA1&pos=999&exon=exon11&mut=3.html"
    soup = BeautifulSoup(open(example, "r").read(), "html.parser")
    wt = soup.findAll("td")[7]
    mutant = soup.findAll("td")[11]
    print wt
    print mutant

    # donor
    example = "html_data/popdon.php?gene=BRCA1&pos=999&exon=exon11&mut=3.html"
    soup = BeautifulSoup(open(example, "r").read(), "html.parser")
    wt = soup.findAll("td")[8]
    mutant = soup.findAll("td")[13]
    print wt
    print mutant


def download():
    base_url = "http://priors.hci.utah.edu/PRIORS/BRCA/viewer.php?gene={0}&exon={1}"
    for gene in ["BRCA1", "BRCA2"]:
        page = urllib.urlopen(base_url.format(gene, "exon2")).read()
        soup = BeautifulSoup(page, "html.parser")
        last_exon = soup.findAll("td", {"class": 'exon'})[-1].a.contents[0]
        for exon in range(2, int(last_exon)+1):
            exon = str(exon)
            print "\n", gene, "exon{0}".format(exon)
            exon_url = base_url.format(gene, "exon" + exon)
            exon_soup = BeautifulSoup(urllib.urlopen(exon_url).read(), "html.parser")
            sequence = exon_soup.findAll("a", {"class": "seq"})
            for base in sequence:
                sys.stdout.write(".")
                sys.stdout.flush()
                position = base.get('href').split("?")[1]
                for splice_type, url_prefix in URL_PREFIX.iteritems():
                    for mutation in ["&mut=1", "&mut=2", "&mut=3"]:
                        this_url = url_prefix + position + mutation
                        filename = "html_data/" + this_url.split("/")[-1] + ".html"
                        with open(filename, "w") as f:
                            f.write(urllib.urlopen(this_url).read())
                            f.close()


if __name__ == "__main__":
    main()
