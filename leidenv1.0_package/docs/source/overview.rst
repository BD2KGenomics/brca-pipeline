.. _overview:

Overview
========

About
^^^^^
The Leiden Open Variation Database platform is a popular genetic variant database platform whose installations are home to
many voluntarily curated mutations implicated in a variety of disease areas.

* A list of all current installations: http://www.lovd.nl/2.0/index_list.php
* LOVD platform: http://www.lovd.nl/3.0/home

Unfortunately these variants are in HGVS format (popular in clinical settings) and in coordinates relative to specific
cDNA transcripts, which makes further analysis difficult informatically. Perhaps more concerning is that the standard
for submission of disease causing mutations was has become much stricter in the time since LOVDs inception.
This implies that there are many false positives within this data set. Curation of these databases is completely voluntary,
making many variants completely unreliable or unusable. Despite these challenges, there are likely many true positives
amongst the noise, many of which may not be in other variant databases. Locating and reporting these true positives is
an important goal for the research community.

While LOVD is public access and has provided reST APIs for querying for variants at specific genomic positions or
retrieving some information about LOVD variants in specific genes, none of the available services allow the actual
variant descriptions (or other submitted information) to be downloaded. This package fills that gap and also facilitates
some degree of data validation.

The goals of this project are to provide tools for:

* Extracting variants from these databases
* Remapping these variants to VCF format
* Cross-checking of information about these variants to infer concordance of submissions

.. important::
    Actually implicating variants as being pathogenic requires thorough manual curation by examining the full set of information
    (including, but not limited to publication references) for validated variants.  "Validation" as described here
    simply implies correctness and consistency of submitted variants, it does not prove true positive implication in any disease.

.. warning::
    The contents of LOVD databases are the intellectual property of the respective curator(s). Any unauthorised use,
    copying, storage or distribution of this material without written permission from the curator(s) will lead to copyright
    infringement with possible ensuing litigation. Copyright © 2013-2014. All Rights Reserved. For further details, refer to
    Directive 96/9/EC of the European Parliament and the Council of March 11 (1996) on the legal protection of databases.

    We have used all reasonable efforts to ensure that the information displayed on these pages and contained in the databases
    is of high quality. We make no warranty, express or implied, as to its accuracy or that the information is fit for a
    particular purpose, and will not be held responsible for any consequences arising out of any inaccuracies or omissions.
    Individuals, organisations and companies which use this database do so on the understanding that no liability whatsoever
    either direct or indirect shall rest upon the curator(s) or any of their employees or agents for the effects of any product,
    process or method that may be produced or adopted by any part, notwithstanding that the formulation of such product, process
    or method may be based upon information here provided.

General Workflow
^^^^^^^^^^^^^^^^
In general, the recommended workflow facilitated by the scripts in this package is:

1. Extract raw variants from LOVD, saving one tab-delimited file per gene.
2. Annotate variants with VEP (must have VEP on path) and combine with original data in a single VCF file per gene.
3. Validate annotated variants by cross-checking submitted data with annotation and output a single VCF for all variants.

The scripts I have included (see :ref:`driver_scripts` and :ref:`other_scripts`) make it easy to carry out this workflow.
There is no need to adhere to this set of scripts if it does not suit your needs. Custom scripts can be developed using
the underlying python packages (see :ref:`packages` for more info)

Project Structure
^^^^^^^^^^^^^^^^^

* /bin/ - contains all scripts (see :ref:`driver_scripts` and :ref:`other_scripts` for more info)
* /leiden/ - python packages for project (see :ref:`packages` for more info)
* /docs/ - project documentation written in the sphinx framework
* /data/ - sample data formats (see :ref:`data` section for more info)

Other folders are for build and distribution purposes.




