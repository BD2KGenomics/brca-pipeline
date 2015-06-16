.. _driver_scripts:

Driver Scripts
==============

In addition to the individual scripts installed with this package, I have also included an example driver script to run
the entire pipeline.

.. important::
    This script runs annotations serially with Variant Effect Predictor, which can take some time to execute. If you
    have access to a distributed computing cluster, you may want to develop your own driver script that runs the
    annotation portion of the pipeline in parallel.

.. tip::
    All scripts are implemented using argparse and have built-in help, which accessible via:

    .. code-block:: bash

        python <script_name>.py --help

run_all.py
^^^^^^^^^^
run_all.py runs the full data extraction and validation process, producing a VCF file with only validated variants.
Discordant variants are saved a separate VCF. See :ref:`data` for more information.


Example Usage
-------------

There are a few use-cases for run_all.py:

1. You are starting completely from scratch (no data has been downloaded from LOVD)

.. code-block:: bash

    python run_all.py -u http://www.dmd.nl/nmdb2/ -output_directory my_output_directory

This will download data from all genes on the specifed LOVD URL, saving one .txt file (``<gene_name>.txt``) with raw data as
well as one VCF file per gene (``<gene_name>_ANNOTATED.vcf``) with variants in VCF format and annotations (Variant Effect Predictor
along with original data from LOVD table).

Note that files are not saved for genes with no listed variants at the specified URL. Variants that fail to remap to VCF
format are saved to ``<gene_name>_remapping_errors.log`` in their original LOVD table format.

2. You already have the txt files containing raw data from LOVD, but want to re-run the rest of the process. Note that
this was primarily useful during development, but may still have some utility for others.

.. code-block:: bash

    python run_all.py --no_download -output_directory my_output_directory

.. note::
    This assumes that the .txt files containing data extracted from LOVD are located in the specified output directory.

3. By default, run_all will not overwrite any existing annotated VCF files. This can be useful if annotation partially completed
and you want to resume, etc. To force an overwrite:

.. code-block:: bash

    python run_all.py --force_overwrite -output_directory my_output_directory
    # OR
    python run_all.py --no_download -output_directory my_output_directory