def format_vcf_text(vcf_format_variants, info_column_entries):
    """
    Create formatted VCF file data from remapped variants.

    Args:
        vcf_format_variants (list of tuples of str): list of tuples that contain chromosome_number, coordinate, ref, alt in that order

        info_column_entries (dict): dictionary where keys are tags to place in info column.
            The values are tuples that contain data_type, description, and a list of values (one per entry in vcf_format_variant)

    Returns:
        list of lists: list of lists where each inner list is a row of the VCF file, and each element in the inner list represents the value of the respective column in a given row.

    """
    # Initialize with required header information for the VCF input to Variant Effect Predictor
    vcf_text = [
        ['##fileformat=VCFv4.0'],
        ['#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO']
    ]

    # Insert INFO tag descriptions into VCF header
    tag_keys = info_column_entries.keys()

    for tag in tag_keys:
        tag_header_text = ''.join(['##INFO=<ID=', tag, ',Number=1,Type=', info_column_entries[tag][0], ',Description="', info_column_entries[tag][1], '">'])
        vcf_text.insert(1, [tag_header_text])

    # Format VCF body text
    for i in range(0, len(vcf_format_variants)):

        chromosome_number, coordinate, ref, alt = vcf_format_variants[i]

        tag_list = []
        for tag in tag_keys:
            tag_value = info_column_entries[tag][2][i].replace(' ', '')
            tag_list.append(tag + '=' + tag_value)

        vcf_file_row = [chromosome_number,
                        coordinate,
                        '.',
                        ref,
                        alt, '.',
                        '.',
                        ';'.join(tag_list)]

        vcf_text.append(vcf_file_row)

    return vcf_text


def read_table_from_file(file_name, column_delimiter='\t'):
    """
    Returns table of data from tab-delimited file. Alternate delimiter can be specified.

    Args:
        file_name (str): path to tab-delimited file wit
        column_delimiter (str, optional): column delimiter (tab by default)

    Returns:
        list of lists: table of data from tab-delimited file
            1st dimension is rows, 2nd is columns

    """

    with open(file_name, 'r') as f:
        file_text = f.read().splitlines()

    return [line.split(column_delimiter) for line in file_text]


def write_table_to_file(file_name, table, column_delimiter='\t'):
    """
    Writes table to tab-delimited file. Alternate delimiter can be specified.

    Args:
        file_name (str): name of output file with extension (can include path)
        column_delimiter (str): column delimiter (tab by default)
        table (list of lists): table data to output to file. 1st dimension is rows, 2nd is columns.

    """

    row_delimiter = '\n'

    file_lines = []

    for row in table:
        file_lines.append(column_delimiter.join(row))

    output_text = row_delimiter.join(file_lines)

    # Ensure unicode strings are encoded before writing
    if isinstance(output_text, unicode):
        output_text = output_text.encode('utf-8')

    with open(file_name, 'w') as f:
        f.write(output_text)