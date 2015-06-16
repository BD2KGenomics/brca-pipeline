from . import vcf
from nose.tools import assert_equals

vcf_lines = ['##INFO=<ID=CSQ,Number=.,Type=String,Description="Consequence type as predicted by VEP. Format: Allele|Gene|Feature|Feature_type|Consequence|cDNA_position|CDS_position|Protein_position|Amino_acids|Codons|Existing_variation|AA_MAF|EA_MAF|EXON|INTRON|MOTIF_NAME|MOTIF_POS|HIGH_INF_POS|MOTIF_SCORE_CHANGE|DISTANCE|STRAND|CLIN_SIG|CANONICAL|SYMBOL|SYMBOL_SOURCE|SIFT|PolyPhen|GMAF|BIOTYPE|ENSP|DOMAINS|CCDS|HGVSc|HGVSp|AFR_MAF|AMR_MAF|ASN_MAF|EUR_MAF|PUBMED">',
             '##INFO=<ID=LOVD,Number=.,Type=String,Description="Consequence type as predicted by VEP. Format: DNA_CHANGE|PROTEIN_CHANGE">',
             vcf.VCF_DELIMTER.join(['#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO']),
             vcf.VCF_DELIMTER.join(['1', '229569803', 'NM_001100.3:c.-66_-65delinsTC', 'AG', 'GA', '.', '.', 'LOVD=NM_001100.3:c.-66_-65delinsTC|p.Arg352Tyr;CSQ=GA|ENSESTG00000008577|ENSESTT00000021605|Transcript|5_prime_UTR_variant|38-39|||||ACTA1:c.-66_-65delinsTC|||1/7|||||||-1||||||||protein_coding|ENSESTP00000021605|||ENSESTT00000021605.1:c.-66_-65delCTinsTC||||||,GA|ENSESTG00000008577|ENSESTT00000021571|Transcript|5_prime_UTR_variant|40-41|||||ACTA1:c.-66_-65delinsTC|||1/4|||||||-1||||||||protein_coding|ENSESTP00000021571|||ENSESTT00000021571.1:c.-66_-65delCTinsTC||||||']),
             ]


def test_get_vcf_dict():

    result = [{'CHROM': '1', 'POS': '229569803', 'ID': 'NM_001100.3:c.-66_-65delinsTC', 'REF': 'AG', 'ALT': 'GA', 'QUAL': '.', 'FILTER': '.',
              'INFO': {
                  'LOVD': {
                        'DNA_CHANGE': 'NM_001100.3:c.-66_-65delinsTC',
                        'PROTEIN_CHANGE': 'p.Arg352Tyr'
                  },

                  'CSQ': {
                    'ENSESTT00000021605': {
                        'AA_MAF': '',
                        'AFR_MAF': '',
                        'ALLELE': 'GA',
                        'AMINO_ACIDS': '',
                        'AMR_MAF': '',
                        'ASN_MAF': '',
                        'BIOTYPE': 'protein_coding',
                        'CANONICAL': '',
                        'CCDS': '',
                        'CDNA_POSITION': '38-39',
                        'CDS_POSITION': '',
                        'CLIN_SIG': '',
                        'CODONS': '',
                        'CONSEQUENCE': '5_prime_UTR_variant',
                        'DISTANCE': '',
                        'DOMAINS': '',
                        'EA_MAF': '',
                        'ENSP': 'ENSESTP00000021605',
                        'EUR_MAF': '',
                        'EXISTING_VARIATION': 'ACTA1:c.-66_-65delinsTC',
                        'EXON': '1/7',
                        'FEATURE': 'ENSESTT00000021605',
                        'FEATURE_TYPE': 'Transcript',
                        'GENE': 'ENSESTG00000008577',
                        'GMAF': '',
                        'HGVSC': 'ENSESTT00000021605.1:c.-66_-65delCTinsTC',
                        'HGVSP': '',
                        'HIGH_INF_POS': '',
                        'INTRON': '',
                        'MOTIF_NAME': '',
                        'MOTIF_POS': '',
                        'MOTIF_SCORE_CHANGE': '',
                        'POLYPHEN': '',
                        'PROTEIN_POSITION': '',
                        'PUBMED': '',
                        'SIFT': '',
                        'STRAND': '-1',
                        'SYMBOL': '',
                        'SYMBOL_SOURCE': ''},

                      'ENSESTT00000021571': {
                          'AA_MAF': '',
                          'AFR_MAF': '',
                          'ALLELE': 'GA',
                          'AMINO_ACIDS': '',
                          'AMR_MAF': '',
                          'ASN_MAF': '',
                          'BIOTYPE': 'protein_coding',
                          'CANONICAL': '',
                          'CCDS': '',
                          'CDNA_POSITION': '40-41',
                          'CDS_POSITION': '',
                          'CLIN_SIG': '',
                          'CODONS': '',
                          'CONSEQUENCE': '5_prime_UTR_variant',
                          'DISTANCE': '',
                          'DOMAINS': '',
                          'EA_MAF': '',
                          'ENSP': 'ENSESTP00000021571',
                          'EUR_MAF': '',
                          'EXISTING_VARIATION': 'ACTA1:c.-66_-65delinsTC',
                          'EXON': '1/4',
                          'FEATURE': 'ENSESTT00000021571',
                          'FEATURE_TYPE': 'Transcript',
                          'GENE': 'ENSESTG00000008577',
                          'GMAF': '',
                          'HGVSC': 'ENSESTT00000021571.1:c.-66_-65delCTinsTC',
                          'HGVSP': '',
                          'HIGH_INF_POS': '',
                          'INTRON': '',
                          'MOTIF_NAME': '',
                          'MOTIF_POS': '',
                          'MOTIF_SCORE_CHANGE': '',
                          'POLYPHEN': '',
                          'PROTEIN_POSITION': '',
                          'PUBMED': '',
                          'SIFT': '',
                          'STRAND': '-1',
                          'SYMBOL': '',
                          'SYMBOL_SOURCE': ''},
                  }
              }}]

    assert_equals(result, vcf.get_vcf_dict(vcf_lines))


def test_get_info_formats():
    input = vcf_lines
    result = {'LOVD': ['DNA_CHANGE', 'PROTEIN_CHANGE'], 'CSQ': ['ALLELE', 'GENE', 'FEATURE', 'FEATURE_TYPE', 'CONSEQUENCE', 'CDNA_POSITION', 'CDS_POSITION', 'PROTEIN_POSITION', 'AMINO_ACIDS', 'CODONS', 'EXISTING_VARIATION', 'AA_MAF', 'EA_MAF', 'EXON', 'INTRON', 'MOTIF_NAME', 'MOTIF_POS', 'HIGH_INF_POS', 'MOTIF_SCORE_CHANGE', 'DISTANCE', 'STRAND', 'CLIN_SIG', 'CANONICAL', 'SYMBOL', 'SYMBOL_SOURCE', 'SIFT', 'POLYPHEN', 'GMAF', 'BIOTYPE', 'ENSP', 'DOMAINS', 'CCDS', 'HGVSC', 'HGVSP', 'AFR_MAF', 'AMR_MAF', 'ASN_MAF', 'EUR_MAF', 'PUBMED']}

    assert_equals(result, vcf._get_info_formats(input))


def test_get_id_string():
    input = '##INFO=<ID=CSQ,Number=.,Type=String,Description="Consequence type as predicted by VEP. Format: Allele|Gene|Feature|Feature_type|Consequence|cDNA_position|CDS_position|Protein_position|Amino_acids|Codons|Existing_variation|AA_MAF|EA_MAF|EXON|INTRON|MOTIF_NAME|MOTIF_POS|HIGH_INF_POS|MOTIF_SCORE_CHANGE|DISTANCE|STRAND|CLIN_SIG|CANONICAL|SYMBOL|SYMBOL_SOURCE|SIFT|PolyPhen|GMAF|BIOTYPE|ENSP|DOMAINS|CCDS|HGVSc|HGVSp|AFR_MAF|AMR_MAF|ASN_MAF|EUR_MAF|PUBMED">'
    result = 'CSQ'

    assert_equals(result, vcf._get_id_string(input))


def test_get_format_string():
    input = '##INFO=<ID=CSQ,Number=.,Type=String,Description="Consequence type as predicted by VEP. Format: Allele|Gene|Feature|Feature_type|Consequence|cDNA_position|CDS_position|Protein_position|Amino_acids|Codons|Existing_variation|AA_MAF|EA_MAF|EXON|INTRON|MOTIF_NAME|MOTIF_POS|HIGH_INF_POS|MOTIF_SCORE_CHANGE|DISTANCE|STRAND|CLIN_SIG|CANONICAL|SYMBOL|SYMBOL_SOURCE|SIFT|PolyPhen|GMAF|BIOTYPE|ENSP|DOMAINS|CCDS|HGVSc|HGVSp|AFR_MAF|AMR_MAF|ASN_MAF|EUR_MAF|PUBMED">'
    result = 'Allele|Gene|Feature|Feature_type|Consequence|cDNA_position|CDS_position|Protein_position|Amino_acids|Codons|Existing_variation|AA_MAF|EA_MAF|EXON|INTRON|MOTIF_NAME|MOTIF_POS|HIGH_INF_POS|MOTIF_SCORE_CHANGE|DISTANCE|STRAND|CLIN_SIG|CANONICAL|SYMBOL|SYMBOL_SOURCE|SIFT|PolyPhen|GMAF|BIOTYPE|ENSP|DOMAINS|CCDS|HGVSc|HGVSp|AFR_MAF|AMR_MAF|ASN_MAF|EUR_MAF|PUBMED'

    assert_equals(result, vcf._get_format_string(input))


def test_normalize_format_string():
    input = 'Allele|gene|Feature-type'
    result = 'ALLELE|GENE|FEATURE_TYPE'

    assert_equals(result, vcf._normalize_format_string(input))


def test_get_info_column_dict():
    raise NotImplementedError('Test not implemented')


def test_get_csq_dict():
    raise NotImplementedError('Test not implemented')


def test_get_lovd_dict():
    raise NotImplementedError('Test not implemented')