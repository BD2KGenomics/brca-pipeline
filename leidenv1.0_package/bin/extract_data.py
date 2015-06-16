# -*- coding: utf-8 -*-
#!/usr/bin/env python

from __future__ import absolute_import
import argparse
import os
from leiden import file_io
from leiden import leiden_database


def extract_data(database, gene_id):
    """
    Extracts variant table data for given gene in leiden_database.

    @param leiden_database: database containing tables of variant data for specified gene_id
    @type leiden_database: LeidenDatabase
    @param gene_id: a string with the Gene ID of the gene to be extracted.
    @type gene_id: string
    @return: tuple containing table entries, column labels.
    @rtype: tuple containing 2D list and list respectively
    @raise: IOError if could not get data
    """

    try:
        gene = database.get_gene_data(gene_id)
        column_labels = gene.columns()
        table_entries = gene.variants()

    except Exception as e:
        raise e

    return table_entries, column_labels

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Given URL to the base URL of any LOVD 2 or 3 database installation, '
                                                 'such as http://www.dmd.nl/nmdb2/, extract variant entries associated with '
                                                 'specified genes. Can specify either a space-separated list of gene names '
                                                 'or -a option to extract data from all genes at the specified URL. Variants '
                                                 'for each gene are saved in a file named according to the gene name they '
                                                 'are associated with.')

    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument('-g', '--genes_available', action="store_true", help='Set to list of all available genes is printed. '
                                                                            'No data is extracted or written to file.')
    group1.add_argument('-a', '--all', default=False, action='store_true',
                        help='Set to extract data for all available genes in the specified Leiden Database.')

    parser.add_argument('-u', '--leiden_url', required=True, help='base URL of the particular Leiden database to be used. For example, '
                                                   'the Leiden muscular dystrophy pages homepage is http://www.dmd.nl/nmdb2/. '
                                                   'This must be a valid URL to base page of database. For example, '
                                                   'http://databases.lovd.nl/whole_genome/ is a valid LOVD3 URL, while '
                                                   'http://databases.lovd.nl/whole_genome/genes is not (it is not the base). '
                                                   'A list of such acceptable URLs is maintained here: '
                                                   'http://www.lovd.nl/2.0/index_list.php')

    parser.add_argument('-l', '--gene_list', help='Gene ID or multiple gene_lists to retrieve from the Leiden Database.', nargs='*')

    parser.add_argument('-o', '--output_directory', default='.', help='Output directory for saved files.')
    args = parser.parse_args()

    # Make the output directory if does not already exist
    output_directory = args.output_directory

    if not os.path.exists(output_directory):
        os.mkdir(args.output_directory)

    genes = None

    if args.genes_available:
        # Print list of available genes to the user
        print("\n".join(leiden_database.make_leiden_database(args.leiden_url)._genes()))

    else:
        # User has specified the all option, extract data from all genes available on the Leiden Database
        if args.all:
            print("---> CHECKING AVAILABLE GENES...")
            genes = leiden_database.make_leiden_database(args.leiden_url)._genes()

        else:
            if len(args.gene_list) > 0:
                genes = args.gene_list
            else:
                print('Must specify at least one gene_list.')

        if genes:
            print '---> Setting things up... '
            database = leiden_database.make_leiden_database(args.leiden_url)

            for gene in genes:
                print '---> ' + gene + ': IN PROGRESS...'
                print '    ---> Downloading data...'

                # Extract table data and save to file
                try:
                    table_data, column_labels = extract_data(database, gene)

                    print '    ---> Saving raw data...'
                    table_data.insert(0, column_labels)
                    output_file_name = os.path.join(output_directory, gene + '.txt')

                    file_io.write_table_to_file(output_file_name, table_data)
                except Exception as e:
                    print '    ---> ' + str(e)

            print '---> All genes complete.'
