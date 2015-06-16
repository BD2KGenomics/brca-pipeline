import re
import pandas as pd
from _ordereddict import ordereddict

VCF_HEADER_PREFIX = '#'
VCF_DELIMITER = '\t'
FORMAT_DELIMITER = '|'


def get_vcf_header_lines(vcf_file):
    """
    Return a list with the header lines from a VCF file.

    Args:
        vcf_file: path to VCF file

    Returns:
        list of str: list of header lines from VCF file

    """

    def stop_loop():
        raise StopIteration

    return list(x.strip("\n") if x.startswith(VCF_HEADER_PREFIX) else stop_loop() for x in vcf_file)


class VCFReader():
    """
    Simple VCF parser that allows dictionary-style parsing of VCF fields and INFO column annotations -- including VEP-like annotations that
    contain a delimited list as their value.

    VCFReaders act as generators and provide one parsed line of output at a time as a VCFLine object.

    Examples:
        vcf = VCFReader(open('file.vcf', 'r'))
        vcf_line = vcf.next()
        vcf_line['REF']  # access REF
        vcf_line['INFO']['CSQ'][1]['Feature']  # access feature of second listing in a VEP-like INFO field
        print str(vcf_line)  # VCFLine objects convert as strings to original format.

    Attributes:
        columns (list of str): list of column names
        header_lines (list of str): list of all header lines from the VCF
        
        infos (dict): dictionary containing IDs from INFO field as primary key
            secondary keys are the Number, Type, description, and format (VEP-like entries only) for INFO field tags.

    """
    def __init__(self, file_object):
        """
        Constructor for VCFReader

        Args:
            file_object (file object): pre-opened file-like object

        """
        self._file_object = file_object
        self.columns = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO']
        self.header_lines = get_vcf_header_lines(self._file_object)
        self.infos = VCFReader.parse_vcf_header(self.header_lines)

    @staticmethod
    def parse_vcf_header(vcf_header_lines):
        """
        Given lines from a VCF header, parse out information from the INFO tags.

        Args:
            vcf_header_lines (list of str): list of header lines from a VCF file.

        Returns:
            dict: a dictionary where each tag is a key and each component (number, type, description, and format
                (only for VEP-like entries with a nested list of fields) of the tag is a secondary key.

        Examples:
            info_dict['MY_TAG']['number']


        """
        infos = {}
        for line in vcf_header_lines:
            if '##INFO' in line:
                id = re.search('ID=([^,]+)\,', line, re.IGNORECASE).group(1)
                number = re.search('Number=([^,]+),', line, re.IGNORECASE).group(1)
                data_type = re.search('Type=([^,]+),', line, re.IGNORECASE).group(1)
                description = re.search('Description="(.+)"', line, re.IGNORECASE).group(1)
                infos[id] = {'number': number, 'type': data_type, 'description': description}

                if 'format' in description.lower():
                    tag_format = re.search('Format: (.+)', description, re.IGNORECASE).group(1)
                    tag_format = VCFReader._normalize_format_string(tag_format)
                    infos[id]['format'] = tag_format.split(FORMAT_DELIMITER)

        return infos

    @staticmethod
    def _normalize_format_string(format_string):
        """
        Returns copy of format_string converted to all uppercase and all non-alphaneumeric characters replaced with underscore

        Args:
            info_header_line (str): format string from tag INFO entry in VCF header

        Returns:
            str: copy of format_string converted to all uppercase and all non-alphaneumeric characters replaced with underscore

        """
        format_string = format_string.upper()
        pattern = re.compile('[^A-Za-z|]')
        return re.sub(pattern, '_', format_string)

    def __iter__(self):
        """
        Allows VCFReaders to be interated over
        """
        return self

    def __next__(self):
        """
        Allows for use as a generator.
        """
        return self.next()

    def next(self):
        """
        Parses the next line of output from the VCF file into a dictionary as described in class description.

        Returns:
            dict: dictionary containing parsed VCF data

        """
        line = self._file_object.next()
        line = line.strip()
        columns = line.split(VCF_DELIMITER)
        vcf_dict = ordereddict(zip(self.columns, columns))

        vcf_dict['INFO'] = self._get_info_dict(vcf_dict['INFO'])
        return VCFLine(vcf_dict)

    def _get_info_dict(self, info_text):
        """
        Helper function to parse the INFO field of a VCF into a dict. VEP-like entries are included as a list of nested
        dictionaries.

        Args:
            info_text (str): text from the INFO column of the VCF

        Returns:
            dict: dict containing parsed data from info_text.

        """
        tags = [x.split('=') for x in info_text.split(';')]
        info_dict = ordereddict(tags)

        for tag in info_dict:
            if 'format' in self.infos[tag]:
                result = []
                for entry in info_dict[tag].split(','):
                    result.append(ordereddict(zip(self.infos[tag]['format'], entry.split(FORMAT_DELIMITER))))
                info_dict[tag] = result
        return info_dict


class VCFLine:
    """
    Class containing information from a single line of a VCF file in a parsed dictionary-style access format.
    This is the type returned by each .next call of the VCFReader generator.

    Examples:
        vcf_line['REF']  # access REF
        vcf_line['INFO']['CSQ'][1]['Feature']  # access feature of second listing in a VEP-like INFO field
        print str(vcf_line)  # VCFLine objects convert as strings to original format.

    """

    def __init__(self, vcf_line):
        self._variant = vcf_line

    def __getitem__(self, var, **args):
        """
        Allows the class to be indexed like dictionary.
        """
        return self._variant[var]

    def __str__(self):
        """
        Custom string conversion for object. Returns line to its initial format.
        """

        info_column = self._variant['INFO']

        values = info_column.values()

        for i,tag_value in enumerate(values):

            if isinstance(tag_value, list):

                inner_entries = []
                for item in tag_value:
                    inner_entries.append(FORMAT_DELIMITER.join(item.values()))

                values[i] = ','.join(inner_entries)

        keys = info_column.keys()
        info = ';'.join(['%s=%s' % (keys[i], value) for i,value in enumerate(values)])
        output_string = self._variant.values()
        output_string[-1] = info
        return '\t'.join(output_string)


def remove_malformed_fields(data_frame):
    """
    Remove garbage entries like NM_35822.3:c.=. p.(=), r.=, etc from all entries stored in a pandas dataframe. Indended
    to pre-process table before converting to VCF format.

    Args:
        data_frame: pandas data frame

    Returns:
        data_frame with all garbage entries replaced with ''

    """

    data_frame = data_frame.replace('.+\.[\(\[\<]?(?:$|=|\?|-|0)[\)\]\>]?(?:$)', '', regex=True)
    return data_frame.replace('^-$', '', regex=True)  # entries with only dashes


def _convert_to_vcf_friendly_text(data_frame):
    """
    Replace characters that are not VCF-friendly in individual fields like ',', FORMAT_DELIMITER, '=', ';', etc. in pandas dataframe.
    Idended to pre-process table before converting to VCF format to ensure quality of output.

    Args:
        data_frame: pandas dataframe

    Returns:
        data_frame with ',', ';', and FORMAT_DELIMITER replaced with '&'. Non-vcf-friendly characters are converted to ''.

    """
    data_frame = data_frame.replace('[=\s]', '', regex=True)
    data_frame = data_frame.replace('[,;|]', '&', regex=True)

    return data_frame


def get_vcf_info_header(data_frame, tag_id, description):
    """
    Returns INFO field header for data in dataframe. Intended for use when want to include all columns in a table as
    fields in a VCF INFO tag. This generates the header text for that INFO tag. Column titles (uppercase) are used as entry names.

    Args:
        data_frame (pandas dataframe): pandas dataframe
        tag_id (str): name for this INFO tag
        description (str): description of this INFO tag

    Returns:
        str: INFO field header for tag

    """

    format_string = FORMAT_DELIMITER.join(data_frame.columns).upper()
    return '##INFO=<ID=' + tag_id + ',Number=.,TYPE=String,Description="' + description + ' Format: ' + format_string + '">'


def _map_to_genomic_coordinates(hgvs_variant, remapper):
    """
    Helper function to use with pandas.DataFrame.apply. Converts HGVS entries to VCF format.

    Args:
        hgvs_variant (str): HGVS formatted variant
        remapper (leiden.remapping.VariantRemapper): VariantRemapper (accepted as parameter because creation is expensive)

    Returns:
        pandas.DataSeries: VCF representation of variant

    """
    try:
        chrom, pos, ref, alt = remapper.hgvs_to_vcf(hgvs_variant)
        return pd.Series({'CHROM': chrom, 'POS': pos, 'ID': hgvs_variant, 'REF': ref, 'ALT': alt})
    except Exception as e:
        return pd.Series({'CHROM': '.', 'POS': '.', 'ID': '.', 'REF': '.', 'ALT': '.'})


def convert_to_vcf_format(data_frame, remapper, hgvs_column, info_tag):
    """
    Converts a pandas dataframe that contains HGVS variants along with other data about the variants to a VCF representation.
    All data fields for each entry are included in the INFO field in info_tag=column1|column2| ... format.

    Args:
        data_frame (pandas.DataFrame): pandas data_frame containing HGVS format variants and other data about said variants
        remapper (leiden.remapping.VariantRemapper): leiden.remapping.VariantRemapper object
        hgvs_column (str): name of the column containing HGVS entries
        info_tag (str): name of the tag to place in the INFO column

    Returns:
        pandas.DataFrame: new dataframe containing variants in VCF format.
            Other columns are included in INFO column as described above.

    """

    data_frame = _convert_to_vcf_friendly_text(data_frame)

    vcf_format = data_frame[hgvs_column].apply(_map_to_genomic_coordinates, args=[remapper])
    info = info_tag + '=' + data_frame.apply(lambda row: FORMAT_DELIMITER.join(map(str, row)), axis=1)
    vcf_format['INFO'] = info
    vcf_format['FILTER'] = '.'
    vcf_format['QUAL'] = '.'

    vcf_format.sort(['CHROM', 'POS'])
    return vcf_format

