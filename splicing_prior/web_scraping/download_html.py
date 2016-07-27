"""
download all html files containing VCFSplicingAnnotator scores
from http://priors.hci.utah.edu/PRIORS/index.php
"""


import urllib
from bs4 import BeautifulSoup



def main():
    #download("http://priors.hci.utah.edu/PRIORS/BRCA/popdon.php?pos=1&gene=BRCA1&x=2&color=A9F5A9&promoted=no&exon=exon2&id=31&mut=3")
    hgvs_positions()


def download(address):
    with open("html_data/example.html", "w") as f: 
       f.write(urllib.urlopen(address).read())
    f.close()

def hgvs_positions():
    """get all the hgvs positions displayed by the priors website"""
    for gene in ["BRCA1", "BRCA2"]:
        url = "http://priors.hci.utah.edu/PRIORS/BRCA/viewer.php?gene={0}&exon=exon2".format(gene)
        page = urllib.urlopen(url).read()
        soup = BeautifulSoup(page, "html.parser")
        print soup.prettify('utf-8')


if __name__ == "__main__":
    main()
