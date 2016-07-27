import urllib




def main():
    download("http://priors.hci.utah.edu/PRIORS/BRCA/popdon.php?pos=1&gene=BRCA1&x=2&color=A9F5A9&promoted=no&exon=exon2&id=31&mut=3")

def download(address):
    print urllib.urlopen(address).read()


if __name__ == "__main__":
    main()
