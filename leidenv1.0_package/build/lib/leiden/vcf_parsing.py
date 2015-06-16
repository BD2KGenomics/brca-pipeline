import re

VCF_DELIMTER = '\t'
FORMAT_DELIMITER = '|'


def get_vcf_dict_from_file(vcf_file):
    """
    Returns a list, where each each element is a nested dictionary providing access to progressively lower-level
    information from a VCF file.

    The first level is the VCF column name (all caps). The info column is a nested dictionary where tag names can be
    accessed. Entries with lists of entries (like VEP) can be accessed in the following order:
    vcf_dict['INFO']['CSQ']['<Transcript_ID>']['<VEP_COLUMN_NAME>' (defined by format in header)]

    Args:
        vcf_file (str): path to VCF file

    Returns:
        list of dict: nested dictionary containing information from each VCF line

    Examples:
        vcf_dict = get_vcf_dict(vcf_file_lines)
        vcf_dict['REF']  # Get REF field
        vcf_dict['INFO']['MY_TAG']  # get tag from INFO field
        vcf_dict['INFO']['CSQ']['NM_0000353.3']['CONSEQUENCE']  # get nested data from tags that contain lists (like VEP)

        Note that VEP lists annotations for a number of features in the same tag. To access each I have indexed results
        by the feature IDs. If you do not know the feature ID, can iterate over all values rather than access via keys.
    """
    vcf_file_lines = [x.strip() for x in open(vcf_file, 'r')]
    return get_vcf_dict(vcf_file_lines)


def get_vcf_dict(vcf_file_lines):
    """
    Returns a list, where each each element is a nested dictionary providing access to progressively lower-level
    information from a VCF file.

    The first level is the VCF column name (all caps). The info column is a nested dictionary where tag names can be
    accessed. Entries with lists of entries (like VEP) can be accessed in the following order:
    vcf_dict['INFO']['CSQ']['<Transcript_ID>']['<VEP_COLUMN_NAME>' (defined by format in header)]

    Args:
        vcf_file_lines (list of str): list of lines from VCF file in original order

    Returns:
        list of dict: nested dictionary containing information from each VCF line

    Examples:
        vcf_dict = get_vcf_dict(vcf_file_lines)
        vcf_dict['REF']  # Get REF field
        vcf_dict['INFO']['MY_TAG']  # get tag from INFO field
        vcf_dict['INFO']['CSQ']['NM_0000353.3']['CONSEQUENCE']  # get nested data from tags that contain lists (like VEP)

        Note that VEP lists annotations for a number of features in the same tag. To access each I have indexed results
        by the feature IDs. If you do not know the feature ID, can iterate over all values rather than access via keys.

    """

    info_formats = _get_info_formats(vcf_file_lines)

    result = []
    for line in vcf_file_lines:
        line.strip()
        if '#' not in line:
            columns = line.split(VCF_DELIMTER)
            column_names = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO']
            vcf_dict = dict(zip(column_names, columns))

            vcf_dict['INFO'] = _get_info_column_dict(vcf_dict['INFO'], info_formats)
            result.append(vcf_dict)
    return result

def get_vcf_header_lines(vcf_file):
    """
    TODO document
    """

    def stop_loop():
        raise StopIteration

    return list(x.strip("\n") if x.startswith('#') else stop_loop() for x in open(vcf_file, 'r'))

def _get_info_column_dict(info_text, info_formats):
    """
    Returns nested dict containing information from the INFO column of VCF. See get_vcf_dict for more info. This is helper
    function to construct the dict nested at vcf_dict['INFO']

    Args:
        info_text (str): text from INFO column of VCF
        info_formats (dict): dict mapping INFO column tag IDs to respective column names

    Returns:
        Returns nested dict containing information from the INFO tag (from VEP) in info column of VCF.

    """

    info_dict = dict([x.split('=') for x in info_text.split(';')])

    info_dict['CSQ'] = _get_csq_dict(info_dict['CSQ'], info_formats)
    info_dict['LOVD'] = _get_lovd_dict(info_dict['LOVD'], info_formats)

    return info_dict


def _get_csq_dict(csq_text, info_formats):
    """
    Returns nested dict containing information from the CSQ tag (from VEP) in info column of VCF. See get_vcf_dict for
    more info. This is helper function to construct the dict nested at vcf_dict['INFO']['CSQ']

    Args:
        csq_text (str): text from CSQ field in INFO column of VCF
        info_formats (dict): dict mapping INFO column tag IDs to respective column names

    Returns:
        Returns nested dict containing information from the CSQ tag (from VEP) in info column of VCF.

    """
    csq_values = [x.split('|') for x in csq_text.split(',')]

    csq_dict = {}
    for transcript in csq_values:
        transcript_dict = dict(zip(info_formats['CSQ'], transcript))
        key = transcript_dict['FEATURE']
        csq_dict[key] = transcript_dict

    return csq_dict


def _get_lovd_dict(lovd_text, info_formats):
    """
    Returns nested dict containing information from the LOVD tag (from LOVD) in info column of VCF. See get_vcf_dict for
    more info. This is helper function to construct the dict nested at vcf_dict['INFO']['LOVD']

    Args:
        lovd_text (str): text from LOVD field in INFO column of VCF
        info_formats (dict): dict mapping INFO column tag IDs to respective column names

    Returns:
        Returns nested dict containing information from the LOVD tag (from LOVD) in info column of VCF.

    """

    lovd_values = lovd_text.split('|')
    lovd_dict = dict(zip(info_formats['LOVD'], lovd_values))

    return lovd_dict


def _get_info_formats(vcf_file_lines):
    """
    Returns a dictionary of INFO column tag IDs to their respective column names from format string.

    Args:
        vcf_file_lines (str): list of lines from VCF file in original order

    Returns:
        dict: a nested dictionary of INFO column tag IDs to their respective column names from format string.

    """
    tag_pattern = re.compile('ID=(.+),')
    format_pattern = re.compile('FORMAT: (.+)"')
    format_dict = {}

    for line in vcf_file_lines:

        if '#' not in line:  # only process header lines
            break

        if '##INFO' in line:
            id = _get_id_string(line)
            format = _get_format_string(line)
            format = _normalize_format_string(format)

            format_dict[id] = format.split('|')
    return format_dict


def _get_id_string(info_header_line):
    """
    Returns ID string from tag INFO entry in VCF header

    Args:
        info_header_line (str): tag INFO entry in VCF header

    Returns:
        str: ID string for tag

    """
    pattern = re.compile('id=(.+),number', re.IGNORECASE)
    match = re.search(pattern, info_header_line)
    return match.group(1)


def _get_format_string(info_header_line):
    """
    Returns format string from tag INFO entry in VCF header

    Args:
        info_header_line (str): tag INFO entry in VCF header

    Returns:
        str: format string for tag

    """
    pattern = re.compile('format: (.+)"', re.IGNORECASE)
    match = re.search(pattern, info_header_line)
    return match.group(1)


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

