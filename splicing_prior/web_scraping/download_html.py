"""
download all html files containing VCFSplicingAnnotator scores
from http://priors.hci.utah.edu/PRIORS/index.php
"""


import urllib
from bs4 import BeautifulSoup


BASE_URL = "http://priors.hci.utah.edu/PRIORS/BRCA/"
URL_PREFIX = {"donor": BASE_URL + "popdon.php?", 
              "acceptor": BASE_URL + "popwtacc.php?"}


def main():
    #download("http://priors.hci.utah.edu/PRIORS/BRCA/popdon.php?pos=1&gene=BRCA1&x=2&color=A9F5A9&promoted=no&exon=exon2&id=31&mut=3")
    hgvs_positions()


def download(address):
    with open("html_data/example.html", "w") as f: 
       f.write(urllib.urlopen(address).read())
    f.close()

def hgvs_positions():
    """get all the hgvs positions displayed by the priors website"""
    base_url = "http://priors.hci.utah.edu/PRIORS/BRCA/viewer.php?gene={0}&exon={1}"
    for gene in ["BRCA1", "BRCA2"]:
        page = urllib.urlopen(base_url.format(gene, "exon2")).read()
        soup = BeautifulSoup(page, "html.parser")
        last_exon = soup.findAll("td", {"class": 'exon'})[-1].a.contents[0]
        for exon in range(2, int(last_exon)+1):
            exon = str(exon)
            print gene, exon
            exon_url = base_url.format(gene, "exon" + exon)
            exon_soup = BeautifulSoup(urllib.urlopen(exon_url).read(), "html.parser")
            sequence = exon_soup.findAll("a", {"class": "seq"})
            for base in sequence:
                position = base.get('href').split("?")[1]
                for splice_type, url_prefix in URL_PREFIX.iteritems():
                    for mutation in ["&mut=1", "&mut=2", "&mut=3"]:
                        this_url = url_prefix + position + mutation
                        print this_url
                    #    page = urllib.urlopen().read()
                break
 
            break
        break



if __name__ == "__main__":
    main()
