.. _other_scripts:

Other Scripts
=============

These scripts are called in sequence by the example driver script - ``run_all.py``. However, they are also callable
individually. Note that the python packages included with this project can also be used to write
entirely new scripts if needed. Feel free to expand and write your own tools!

.. tip::
    Note all scripts are made with argsparse, so contain built-in help. To access help simply execute: ``python <script_name>.py --help``

.. important::
    The leiden package must be installed or on your PYTHONPATH to run these scripts.

extract_data.py
^^^^^^^^^^^^^^^
extract_data.py allows raw data from the any leiden open variation database installation to be downloaded
and saved to text files (one per gene). There are options to allow either data from all genes or a specific list of genes
to be downloaded as needed. It also allows users to print a list of all available genes at a given URL, which is useful
if you want to check what is available.

.. note::
    Note that both LOVD versions 2 and 3 are supported for this script.

Example Usage
-------------

Download data for all genes from a given url to a specified output directory:

.. code-block:: bash

    python extract_data.py --all --leiden_url http://www.dmd.nl/nmdb2/ --output_directory my_directory

Download a list of specified genes from a given url to a specified output directory:

.. code-block:: bash

    python extract_data.py --leiden_url http://www.dmd.nl/nmdb2/ --output_directory my_directory --gene_list ACTA1 DYSF

Print a list of available genes at a specified URL:

.. code-block:: bash

    python extract_data.py --genes_available --leiden_url http://www.dmd.nl/nmdb2/

generate_annotated_vcf.py
^^^^^^^^^^^^^^^^^^^^^^^^^
This script utilizes VEP to annotate variants and output a VCF file (<original_file_name>.vcf). The original data from tables of data downloaded from
LOVD are also added to the VCF in a format similar to VEP's CSQ tag in VCF annotation. Variants that could not be converted
to VCF format are not saved to output file.

Example Usage
-------------

Run on list of files contained in a file (improved efficiency over multiple script calls):

.. code-block:: bash

    python generate_annotated_vcfs.py -f file_names.txt


validate_annotated_vcfs.py
^^^^^^^^^^^^^^^^^^^^^^^^^^

This script takes either a single file or a list of annotated VCF files as input and outputs a single VCF file with
all concordant variants from all input files. Variants that are not concordant are saved to a separate VCF.

How is concordance determined?

VEP provides a HGVS protein change prediction, which is compared to the protein change reported in LOVD. If neither
LOVD or VEP report a protein change (intronic variants, splice variants, etc.), we instead... TODO

Example Usage
-------------

Using a file containing names of all input files:

.. code-block:: bash

    python extract_data.py --output_file output.vcf --discordant_output_file discordant.vcf -f file_list.txt