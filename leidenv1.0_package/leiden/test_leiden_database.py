from nose.tools import assert_equals
from . import leiden_database
from mock import Mock
import web_io
import canned_html_responses as responses


def mock_html_response(database, gene_homepage_response, variant_database_response):
    """
    Helper function to mock the HTML responses for given database
    """
    database._get_gene_homepage_html = Mock(return_value=gene_homepage_response)
    database._get_variant_database_html = Mock(return_value=variant_database_response)
    return database


def test_extract_lovd_version_number_with_lovd_2():
    input = 'http://www.dmd.nl/nmdb2/'
    result = 2.0
    web_io.get_page_html = Mock(return_value=responses.NMDB2_HOMEPAGE_HTML)
    assert_equals(result, leiden_database._extract_lovd_version_number(input))


def test_extract_lovd_version_number_with_lovd_3():
    input = 'http://mseqdr.lumc.edu/GEDI/'
    result = 3.0
    web_io.get_page_html = Mock(return_value=responses.GEDI_HOMEPAGE_HTML)
    assert_equals(result, leiden_database._extract_lovd_version_number(input))


class TestLOVD2DatabaseACTA1():

    @classmethod
    def setup_class(cls):
        web_io.get_page_html = Mock(return_value=responses.NMDB2_HOMEPAGE_HTML)
        leiden_database._LOVD2GeneData = mock_html_response(leiden_database._LOVD2GeneData, responses.ACTA1_GENE_HOMEPAGE_HTML, responses.ACTA1_VARIANT_DATABASE_HTML)
        cls.database = leiden_database._LOVD2Database('http://www.dmd.nl/nmdb2/')
        cls.gene = cls.database.get_gene_data('ACTA1')

    def test_get_lovd_version(cls):
        # Static method, not overridden in subclasses
        pass

    def test_get_version_number(cls):
        result = 2
        assert_equals(cls.database.version_number(), result)

    def test_get_variant_database_url_with_acta1(cls):
        result = 'http://www.dmd.nl/nmdb2/variants.php?action=search_unique&select_db=ACTA1&limit=1000'
        assert_equals(cls.gene._get_variant_database_url(), result)

    def test_get_gene_homepage_url(cls):
        result = 'http://www.dmd.nl/nmdb2/home.php?select_db=ACTA1'
        assert_equals(cls.gene._get_gene_homepage_url(), result)

    def test_get_transcript_refseqid_with_acta1(cls):
        result = 'NM_001100.3'
        assert_equals(cls.gene.transcript_refseqid(), result)

    def test_get_table_headers(cls):
        result = ['exon', 'dna_change', 'var_pub_as', 'rna_change', 'codon_change', 'protein_change', 'db_id',
                  'variant_remarks', 'genet_ori', 'reference', 'template', 'technique', 'frequency', 're_site']
        assert_equals(cls.gene.columns(), result)

    def test_get_table_data(cls):
        result = responses.ACTA1_TABLE_DATA
        #assert_equals(cls.gene.variants(), result)   # very slow -- must be accessing network
        raise NotImplementedError()


class TestLOVD2DatabaseCAPN3():

    @classmethod
    def setup_class(cls):
        web_io.get_page_html = Mock(return_value=responses.NMDB2_HOMEPAGE_HTML)
        leiden_database._LOVD2GeneData = mock_html_response(leiden_database._LOVD2GeneData, responses.CAPN3_GENE_HOMEPAGE_HTML, responses.CAPN3_VARIANT_DATABASE_HTML)
        cls.database = leiden_database._LOVD2Database('http://www.dmd.nl/nmdb2/')
        cls.gene = cls.database.get_gene_data('CAPN3')

    def test_get_lovd_version(cls):
        # Static method, not overridden in subclasses
        pass

    def test_get_version_number(cls):
        result = 2
        assert_equals(cls.database.version_number(), result)

    def test_get_variant_database_url_with_capn3(cls):
        result = 'http://www.dmd.nl/nmdb2/variants.php?action=search_unique&select_db=CAPN3&limit=1000'
        assert_equals(cls.gene._get_variant_database_url(), result)

    def test_get_gene_homepage_url_with_capn3(cls):
        result = 'http://www.dmd.nl/nmdb2/home.php?select_db=CAPN3'
        assert_equals(cls.gene._get_gene_homepage_url(), result)

    def test_get_gene_homepage_url(cls):
        result = 'http://www.dmd.nl/nmdb2/home.php?select_db=CAPN3'
        assert_equals(cls.gene._get_gene_homepage_url(), result)

    def test_get_transcript_refseq_id_with_capn3(cls):
        result = 'NM_000070.2'
        assert_equals(cls.gene.transcript_refseqid(), result)

    def test_get_table_headers(cls):
        result = ['exon', 'dna_change', 'var_pub_as', 'rna_change', 'protein_change', 'db_id', 'variant_remarks',
                  'genet_ori', 'segregation', 'reference', 'template', 'technique', 'frequency', 're_site']

        assert_equals(cls.gene.columns(), result)

    def test_get_table_data(cls):
        result = responses.CAPN3_TABLE_DATA
        #assert_equals(cls.genes.variants(), result)  # very slow -- must be accessing network
        raise NotImplementedError()

class TestLOVD3DatabaseBBS1():

    @classmethod
    def setup_class(cls):
        web_io.get_page_html = Mock(return_value=responses.GEDI_HOMEPAGE_HTML)
        leiden_database._LOVD3GeneData = mock_html_response(leiden_database._LOVD3GeneData, responses.BBS1_GENE_HOMEPAGE_HTML, responses.BBS1_VARIANT_DATABASE_HTML)
        cls.database = leiden_database._LOVD3Database('http://mseqdr.lumc.edu/GEDI/')
        cls.gene = cls.database.get_gene_data('BBS1')

    def test_get_version_number_with_bbs1(cls):
        result = 3
        assert_equals(cls.database.version_number(), result)

    def test_get_variant_database_url(cls):
        result = 'http://mseqdr.lumc.edu/GEDI/variants/BBS1?page_size=1000&page=1'
        assert_equals(cls.gene._get_variant_database_url(), result)

    def test_get_gene_homepage_url(cls):
        result = 'http://mseqdr.lumc.edu/GEDI/genes/BBS1?page_size=1000&page=1'
        assert_equals(cls.gene._get_gene_homepage_url(), result)

    def test_get_transcript_refseqid(cls):
        result = 'NM_024649.4'
        assert_equals(cls.gene.transcript_refseqid(), result)

    def test_get_table_headers(cls):
        # This gene does not have any entries -- should return []
        result = []

        assert_equals(cls.gene.columns(), result)

    def test_get_table_data(cls):
        # This gene does not have any entries -- should return []
        result = responses.BBS1_TABLE_DATA

        assert_equals(cls.gene.variants(), result)


class TestLOVD3DatabaseCTC1():

    @classmethod
    def setup_class(cls):
        web_io.get_page_html = Mock(return_value=responses.GEDI_HOMEPAGE_HTML)
        leiden_database._LOVD3GeneData = mock_html_response(leiden_database._LOVD3GeneData, responses.CTC1_GENE_HOMEPAGE_HTML, responses.CTC1_VARIANT_DATABASE_HTML)
        cls.database = leiden_database._LOVD3Database('http://mseqdr.lumc.edu/GEDI/')
        cls.gene = cls.database.get_gene_data('CTC1')

    def test_get_version_number(cls):
        result = 3
        assert_equals(cls.database.version_number(), result)

    def test_get_variant_database_url(cls):
        result = 'http://mseqdr.lumc.edu/GEDI/variants/CTC1?page_size=1000&page=1'
        assert_equals(cls.gene._get_variant_database_url(), result)

    def test_get_gene_homepage_url(cls):
        result = 'http://mseqdr.lumc.edu/GEDI/genes/CTC1?page_size=1000&page=1'
        assert_equals(cls.gene._get_gene_homepage_url(), result)

    def test_get_transcript_refseqid(cls):
        result = 'NM_025099.5'
        assert_equals(cls.gene.transcript_refseqid(), result)

    def test_get_table_headers(cls):
        result = ['effect', 'exon', 'dna_change', 'rna_change', 'protein_change', 'dna_change_genomic', 'reference',
                  'db_id', 'dbsnp_id', 'frequency', 'inote', 'owner']

        assert_equals(cls.gene.columns(), result)

    def test_get_table_data(cls):
        result = responses.CTC1_TABLE_DATA
        assert_equals(cls.gene.variants(), result)