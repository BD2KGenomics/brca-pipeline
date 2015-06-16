import re
import math

from bs4 import BeautifulSoup
from . import web_io, utilities


def make_leiden_database(leiden_url):
    """
    Factory method that returns appropriate LeidenDatabase object for lovd version installed at specified URL.
    Only LOVD2 and LOVD3 installations are supported.

    Args:
        leiden_url(str): The base URL of the particular Leiden lovd to be used.
            For example, the Leiden muscular dystrophy pages LOVD2 homepage is http://www.dmd.nl/nmdb2/. This must be a
            valid URL to base page of lovd. For LOVD3 installations, such as the Genetic Eye Disorder (GEI) Variation
            Database, the base url will be similar to http://mseqdr.lumc.edu/GEDI/. Extensions of this URL, such as
            http://mseqdr.lumc.edu/GEDI/genes or http://mseqdr.lumc.edu/GEDI/variants should not be used.
        gene_id (str): a string with the Gene ID of the gene of interest. For example, ACTA1 is the gene ID for
            actin, as specified on the Leiden Muscular Dystrophy Pages at http://www.dmd.nl/nmdb2/home.php?

    Returns:
        LeidenDatabase: LeidenDatabase object for specified URL and gene.

    Raises:
        Exception: If the lovd version installed at specified URL is unsupported (anything other than version 2 or 3)

    """

    version = _extract_lovd_version_number(leiden_url)

    # Generate instance of appropriate _LeidenDatabase subclass for installed version
    if version == 2:
        database = _LOVD2Database(leiden_url)
    elif version == 3:
        database = _LOVD3Database(leiden_url)
    else:
        raise Exception("Unrecognized LOVD version number: " + str(version) + "!")

    return database


def _extract_lovd_version_number(leiden_url):
    """
    Extract the version number of the lovd installation at the specified URL.

    Args:
        leiden_url (str): the base URL of the particular Leiden lovd to be used.
            For example, the Leiden muscular dystrophy pages homepage is http://www.dmd.nl/nmdb2/. This must be a
            valid URL to base page of lovd.

    Returns:
        float: lovd version number

    """

    html = web_io.get_page_html(leiden_url)

    # Extract the version number from HTML
    try:
        regex = re.compile('LOVD v\.([23])\.\d', re.IGNORECASE)
        results = regex.search(html)
        version_number = results.group(1)
    except Exception as e:
        raise ValueError('No version number detected at specified URL')

    return float(version_number)


class LeidenDatabase:
    """
    Should not construct directly. Use make_leiden_database factory method to obtain instances of LeidenDatabase objects.

    Class providing functions to extract information about a variants listed under a specified gene on a specified lovd
    Leiden Database installation. For example, http://www.dmd.nl/nmdb2/, is a particular installation for
    variants in genes associated with Muscular Dystrophy. A list of all known installations of lovd databases can be
    found at http://www.lovd.nl/2.0/index_list.php.

    """

    def __init__(self, leiden_url):
        """
        Initializes a LeidenDatabase object for the specified Leiden Database URL and gene.

        Args:
            leiden_url (str): the base URL of the particular Leiden lovd to be used.
                For example, the Leiden muscular dystrophy pages homepage is http://www.dmd.nl/nmdb2/. This must be a valid URL to base page of lovd.

        Raises:
            ValueError: if gene does not exist in the specified Leiden Database

        """
        self._leiden_url = leiden_url
        self._version_number = None
        self._available_genes = None

    def version_number(self):
        """
        Return version number of lovd in use for lovd.

        Returns:
            float: version number of lovd in use for lovd

        """

        return self._version_number

    def genes(self):
        """
        Returns a list of gene IDs available on this database.

        Returns:
            list of str: list of gene IDs available on this database.

        """
        return self._available_genes

    def _genes(self):
        """
        Helper function to get a list of available genes. Returns a list of gene IDs available on this database.

        Returns:
            list of str: list of gene IDs available on this database.

        """
        raise NotImplementedError('Abstract method')

    def get_gene_data(self, gene_id):
        """
        Returns a _GeneData object that provides a interface to data on the specified gene. Available functions allow
        access to variants, column labels, reference transcript, etc. See _GeneData for documentation.

        Args:
            gene_id (str): a string with the Gene ID of the gene of interest. For example, ACTA1 is the gene ID for
                actin, as specified on the Leiden Muscular Dystrophy Pages at http://www.dmd.nl/nmdb2/home.php?

        Returns:
            _GeneData: _GeneData object for specified gene ID.

        """
        raise NotImplementedError('Abstract method')


class _LOVD2Database(LeidenDatabase):
    """
    Should not construct directly. Use make_leiden_database factory method to obtain instances of LeidenDatabase objects.

    Provides LeidenDatabse interface specific to LOVD version 2. See LeidenDatabase super class for function documentation.
    """

    def __init__(self, leiden_url):

        # Call to the super class constructor
        LeidenDatabase.__init__(self, leiden_url)
        self._version_number = 2
        self._available_genes = self._genes()

    def _genes(self):
        # Construct URL of page containing the drop-down to select various genes
        start_url = "".join([self._leiden_url, '?action=switch_db'])

        # Download and parse HTML from base URL
        html = web_io.get_page_html(start_url)
        url_soup = BeautifulSoup(html)

        # Extract all options from the SelectGeneDB drop-down control
        options = url_soup.find(id='SelectGeneDB').find_all('option')

        # Return all options in the drop-down
        available_genes = []
        for genes in options:
            available_genes.append(genes['value'])
        return available_genes

    def get_gene_data(self, gene_id):
        if gene_id in self._available_genes:
            return _LOVD2GeneData(self._leiden_url, gene_id)
        else:
            raise ValueError('Specified gene ID not found on database: %s' % gene_id)


class _LOVD3Database(LeidenDatabase):
    """
    Should not construct directly. Use make_leiden_database factory method to obtain instances of LeidenDatabase objects.

    Provides LeidenDatabase interface specific to lovd version 3. See LeidenDatabase super class for function documentation.
    """

    def __init__(self, leiden_url):

        # Call to the super class constructor
        LeidenDatabase.__init__(self, leiden_url)
        self._version_number = 3
        self._available_genes = self._genes()

    def _genes(self):
        # Construct URL of page containing the drop-down to select various genes
        start_url = "".join([self._leiden_url, 'genes/', '?page_size=1000&page=1'])

        # Download and parse HTML from base URL
        html = web_io.get_page_html(start_url)
        url_soup = BeautifulSoup(html)

        # Extract all gene entries from the lovd homepage
        table_class = 'data'
        options = url_soup.find_all('tr', class_=table_class)

        available_genes = []
        for genes in options:
            gene_string = genes.find_all('td')[0].find('a').string
            available_genes.append(gene_string)
        return available_genes

    def get_gene_data(self, gene_id):
        if gene_id in self._available_genes:
            return _LOVD3GeneData(self._leiden_url, gene_id)
        else:
            raise ValueError('Specified gene ID not found on database: %s' % gene_id)


class GeneData:
    """
    Should not construct directly. Use get_gene_data method of LeidenDatabase objects constructed with make_leiden_database
    to construct.

    Class for interfacing with data provided on genes on LOVD installations.
    """

    def __init__(self, leiden_url, gene_id):
        """
        Constructor for _GeneData. Should not construct directly. Use get_gene_data method of LeidenDatabase objects
        constructed with make_leiden_database to construct.

        leiden_url (str): the base URL of the particular Leiden lovd to be used.
            For example, the Leiden muscular dystrophy pages homepage is http://www.dmd.nl/nmdb2/. This must be a valid URL to base page of lovd.
        gene_id (str): a string with the Gene ID of the gene of interest. For example, ACTA1 is the gene ID for
            actin, as specified on the Leiden Muscular Dystrophy Pages at http://www.dmd.nl/nmdb2/home.php?

        """

        self._leiden_home_url = leiden_url
        self._gene_id = gene_id

        # Extract HTML and create BeautifulSoup objects for gene_id pages
        html = self._get_variant_database_html()
        self._database_soup = BeautifulSoup(html)

        html = self._get_gene_homepage_html()
        self._gene_homepage_soup = BeautifulSoup(html)

    def _get_variant_database_url(self):
        """
        Constructs URL linking to the table of variant entries for this gene.

        Returns:
            str: URL linking to the table of variant entries for the specified gene_id on the Leiden Database site.

        """

        raise NotImplementedError('Abstract method')

    def _get_variant_database_html(self):
        """
        Returns the page html from the table of variant entries for this gene.

        Returns:
            str: html from the table of variant entries for this gene.

        """
        url = self._get_variant_database_url()
        return web_io.get_page_html(url)

    def _get_gene_homepage_url(self):
        """
        Constructs the URL linking to the homepage for this gene.

        Returns:
            str: URL linking to the homepage for this gene.

        """

        raise NotImplementedError('Abstract method')

    def _get_gene_homepage_html(self):
        """
        Returns the page html from the homepage for this gene.

        Returns:
            str: html from the homepage for this gene.

        """
        url = self._get_gene_homepage_url()
        return web_io.get_page_html(url)

    def _get_link_urls(self, link_result_set):
        """
        Given a BeautifulSoup ResultSet object containing only link tags, return the URLs as a list.

        Args:
            link_result_set (BeautifulSoup ResultSet): a collection of links.
                All tags must be passed as a BeautifulSoup ResultSet object. This is the type of object returned by
                methods such as find_all in BeautifulSoup. See http://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all
                for more information.

        Returns:
            list of str: list of URLs from link_result_set

        """
        link_delimiter = ','
        result = []
        transcript_id = self.transcript_refseqid()
        for links in link_result_set:
            link_url = links.get('href')

            # Process HGVS notation
            if links.string and ('c.' in links.string or 'p.' in links.string):
                hgvs_notation = utilities.remove_times_reported(links.string)
                hgvs_notation = utilities.correct_hgvs_parentheses(hgvs_notation)
                result.append("".join([transcript_id, ':', hgvs_notation]))
            elif links.string:
                result.append(link_url)

        return link_delimiter.join(result)

    @staticmethod
    def _normalize_label(label):
        """
        Normalizes column labels to ensure they are in as consistent a format as possible.

        Args:
            label (str): column label

        Returns:
            label in all lowercase, all non-alphaneumeric characters converted to '_', and common variations of dna_change,
            protein_change, and dna_change_genomic converted to consistent naming.

        """
        label = label.lower().strip()
        label = re.sub(re.compile('[^A-Za-z0-9]'), '_', label)

        # Some databases do not have consistent headers
        if 'protein' in label:
            label = 'protein_change'
        elif 'genomic' in label:
            label = 'dna_change_genomic'
        elif 'dna' in label:
            label = 'dna_change'

        return label

    def transcript_refseqid(self):
        """
        Returns the transcript refSeq ID for gene (denoted by NM_<ID> on the gene homepage on the given gene_id).
        For example, the ACTA1 homepage is http://www.dmd.nl/nmdb2/home.php and the RefSeq ID is "NM_001100.3".

        Returns:
            string: transcript refSeqID for set gene. Returns an empty string if no refSeq ID is found.

        """

        # Find all links on the gene homepage
        entries = self._gene_homepage_soup.find_all('a')
        for tags in entries:
            # NM_ is unique substring to RefSeq ID. If found, return text.
            if 'NM_' in tags.get_text():
                return tags.get_text()
        return ''

    def columns(self):
        """
        Returns the column labels from the table of variants in the Leiden Database for the set gene.

        Returns:
            list of str: column labels from the table of variants in the Leiden Database variant listing for the object's gene_id.
                Returned in left to right order as they appear on the Leiden Database. Empty list returned if no labels are found.

        """

        raise NotImplementedError('Abstract method')

    def variants(self):
        """
        Returns the table of variants for gene.

        Returns:
            list of list of str: table of variants from the gene
                1st dimension is rows, 2nd is columns

        """

        total_variant_count = self.variant_count()

        # Calculate the number of pages website will use to present data
        variants_per_page = 1000  # max allowed value
        total_pages = int(math.ceil(float(total_variant_count)/float(variants_per_page)))

        # Get table data from all pages
        table_data = []
        for page_number in range(1, total_pages + 1):
            table_data.extend(self._variants_page_n(page_number))

        return table_data

    def _variants_page_n(self, page_number):
        """
        Returns the table data from a specified page of the table of variant entries. Each page number (positive integer)
        has 1000 variants at most. The requested page number should not exceed the number of pages required to display
        the total number of variants.

        Args:
            page_number (int): page number containing the desired table data.

        Returns:
            list of list of str: table of variants from the set gene on the Leiden Database from the nth page.

        """

        raise NotImplementedError('Abstract method')

    def variant_count(self):
        """
        Get the total number of variants for gene. This is the total number of variant entries in table of variants,
        not the number of unique entries.

        Returns:
            int: Number of variants listed for current gene

        Raises:
            ValueError: if the number of entries could not be found on web page

        """

        # Search for sequences of digits that are four digits or longer in length.
        m = re.compile('(\d+)\s(?:entries|entry)')
        results = m.search(self._database_soup.get_text())

        # Return entire matched sequence (PMID)
        if results is not None:
            return int(results.group(1))
        else:
            raise ValueError('No entries found at given URL')


class _LOVD2GeneData(GeneData):
    """
    Should not construct directly. Use get_gene_data method of LeidenDatabase objects constructed with make_leiden_database
    to construct.

    Provides GeneData interface specific to lovd version 2. See GeneData super class for function documentation.
    """

    def __init__(self, leiden_url, gene_id):
        GeneData.__init__(self, leiden_url, gene_id)

    def _get_variant_database_url(self):

        return "".join([self._leiden_home_url, 'variants.php?action=search_unique&select_db=', self._gene_id,
                        '&limit=1000'])

    def _get_gene_homepage_url(self):

        return "".join([self._leiden_home_url, 'home.php?select_db=', self._gene_id])

    def columns(self):

        # Find all th tags on the table of variants (column labels)
        headers = self._database_soup.find_all('th')
        result = []
        for entries in headers:
            # Column label text
            h = entries.string

            # For all entries with a string value, add them to the results (filters out extraneous th tags)
            if h is not None:
                # Normalize headers so all lower-case, no whitespace, no non-alphanumeric characters
                h = GeneData._normalize_label(h)
                result.append(h)

        return result

    def _variants_page_n(self, page_number):

        # TODO this is somewhat redundant w/ other subclass
        if page_number is not 1:

            page_url = self._get_variant_database_url() + '&page=' + str(page_number)

            html = web_io.get_page_html(page_url)
            database_soup = BeautifulSoup(html)
        else:
            database_soup = self._database_soup

        # id specific to data table in HTML (must be unicode due to underscore)
        table_id = "".join([u'table', u'\u005F', u'data'])

        # Extract the HTML specific to the table data
        table = database_soup.find_all(id=table_id)[0].find_all('tr')

        # First row may contain a row of images for some reason. Filter out if present.
        if table[0].find('img') is not None:
            table = table[1:]

        row_entries = []
        for rows in table:
            entries = []
            for columns in rows.find_all('td'):
                # If there are any links in the cell, process them with get_link_info
                if columns.find('a') is not None:
                    link_string = self._get_link_urls(columns.find_all('a'))
                    link_string = re.sub(r'\s', '', link_string)  # ensure there is no whitespace
                    entries.append(link_string)
                else:
                    column_string = columns.string.strip()  # ensure there is no whitespace
                    column_string = re.sub(r'\s', ' ', column_string)
                    entries.append(column_string)
            row_entries.append(entries)
        return row_entries


class _LOVD3GeneData(GeneData):
    """
    Should not construct directly. Use get_gene_data method of LeidenDatabase objects constructed with make_leiden_database
    to construct.

    Provides GeneData interface specific to lovd version 3. See GeneData super class for function documentation.
    """

    def __init__(self, leiden_url, gene_id):
        GeneData.__init__(self, leiden_url, gene_id)

    def _get_variant_database_url(self):

        return "".join([self._leiden_home_url, 'variants/', self._gene_id, '?page_size=1000&page=1'])

    def _get_gene_homepage_url(self):

        return "".join([self._leiden_home_url, 'genes/', self._gene_id, '?page_size=1000&page=1'])

    def columns(self):

        # Find all th tags on the table of variants (column labels)
        headers = self._database_soup.find_all('th')
        result = []
        for entries in headers:
            # Column label text
            h = entries.text

            # For all entries with a string value, add them to the results (filters out extraneous th tags)
            if h is not None:
                h = GeneData._normalize_label(h)
                result.append(h)

        return result

    def _variants_page_n(self, page_number):

        # TODO this is somewhat redundant w/ other subclass
        if page_number is not 1:

            page_url = self._get_variant_database_url() + '&page=' + str(page_number)

            html = web_io.get_page_html(page_url)
            database_soup = BeautifulSoup(html)
        else:
            database_soup = self._database_soup

        # id specific to data table in HTML (must be unicode due to underscore)
        table_class = u'data'

        # Extract the HTML specific to the table data
        table = database_soup.find_all('tr', class_=table_class)

        if table:
            pass
        else:
            table = database_soup.find_all('tr', class_='marked')  # some LOVD3 pages had a different class

        # First row may contain a row of images for some reason. Filter out if present.
        if table[0].find('img') is not None:
            table = table[1:]

        row_entries = []
        for rows in table:
            # Difficult to exclude column label images, as they are included as a table row with no identifier. They
            # all contain images, while none of the data rows do. This allows column label row to be filtered out.
            entries = []
            for columns in rows.find_all('td'):
                # If there are any links in the cell, process them with get_link_info
                if columns.find('a') is not None:
                    link_string = self._get_link_urls(columns.find_all('a'))
                    link_string = re.sub(r'\s', '', link_string)  # ensure there is no whitespace
                    entries.append(link_string)
                else:
                    column_string = columns.string.strip()
                    column_string = re.sub(r'\s', ' ', column_string)  # ensure there is no non-space whitespace
                    entries.append(column_string)
            row_entries.append(entries)
        return row_entries