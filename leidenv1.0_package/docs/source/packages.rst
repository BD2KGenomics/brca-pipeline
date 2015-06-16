.. _packages:

Modules
=======
This project contains a number of distinct python modules.

Note that there are tests for most modules that are not simple wrappers for other scripts or libraries. These tests are
included alongside modules in files named ``test_<module_name>.py``. These tests are not 100% comprehensive.

Tests are compatible with the nose unit testing platform. This is an extension of the default unittest platform that makes
tests very easy to develop and run. To run all unit tests for this project run the following from the root directory.

.. code-block:: python

    nosetests


Note that the nose python package must be installed to run tests. Tests for specific individual modules can also be run.
Please see nose documentation for more information.

.. tip::
    The scripts included with this package provide example usage of the functions in these modules.

leiden_database
^^^^^^^^^^^^^^^
These classes allow a user to extract tables of data (mutations listed for a specific gene in the database) and other
useful information from any Leiden Open Variation Database (LOVD) installation, such as http://www.dmd.nl/nmdb2/. Unfortunately,
it has been necessary to do this by downloading the HTML for relevant pages on the database and parsing out the necessary
data, as they do not provide an easy way to access the data otherwise. Note that I have chosen to use beautifulsoup4 internally
for HTML parsing.

The usage for these classes is as follows:

.. code-block:: python

    leiden_url = 'http://www.dmd.nl/nmdb2/'  # base URL of LOVD installation
    gene_id = 'ACTA1'  # External name for Gene

    database = make_leiden_database(leiden_url)  # factory method automatically chooses right database version
    database.genes()  # get a list of available genes
    database.version()  # get LOVD version

    # Get data about a gene
    acta1 = database.get_gene_data(gene_id)
    reference_transcript = acta1.transcript_refseqid()
    number_of_variants = acta1.variant_count()
    column_labels = acta1.columns()  # get column labels
    variants = acta1.variants()  # get table of all variants


Note that make_leiden_database returns a LeidenDatabase object. There are two subclasses of this type (one for each
version of LOVD). This method ensures that the correct subclass is chosen for the provided URL.

Unit tests for this module are currently quite slow because they actually make requests for HTML data. Ideally, this
would be replaced with Mock Objects where we have canned HTML responses saved on disk.

Member Descriptions
+++++++++++++++++++

.. automodule:: leiden.leiden_database
   :members:


utilities
^^^^^^^^^
These are general utility functions, some of which are used in leiden_database.py as general purpose functions.

Member Descriptions
+++++++++++++++++++

.. automodule:: leiden.utilities
   :members:

file_io
^^^^^^^
This module has functions for reading and writing delimited files to and from 2D lists where first dimension is rows and
the second is columns.

Member Descriptions
+++++++++++++++++++

.. automodule:: leiden.file_io
   :members:

web_io
^^^^^^
This module has functions for reading HTML data from URLs. Essentially, this is just wrapping the library used to
make HTML requests to make it easier to change if needed.

Member Descriptions
+++++++++++++++++++

.. automodule:: leiden.web_io
   :members:


annotate_vcf
^^^^^^^^^^^^
This module provides a function to run Variant Effect Predictor annotation on VCF files.

Member Descriptions
+++++++++++++++++++

.. automodule:: leiden.annotate_vcf
   :members:


validation
^^^^^^^^^^
This module contains functions that are used to help with validation of annotated variants.

.. automodule:: leiden.validation
    :members:


vcf
^^^
This module contains functions for parsing VCF files, providing data structures that provide easier access to information
in annotated VCF files, and converting pandas dataframes with HGVS notation variants and associated data to VCF format.

.. automodule:: leiden.vcf
    :members:

