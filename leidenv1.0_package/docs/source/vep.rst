.. _vep:

Variant Effect Predictor
========================

In order to run the annotation and validation software in leiden, you must have Variant Effect Predictor (VEP) installed and available on your PATH.

.. important::
    Make sure variant_effect_predictor.pl is on your PATH!

Currently, the parameters for VEP are hard-coded and as follows:

.. code-block:: bash

    --vcf
    --cache
    --fork 4
    --host useastdb.ensembl.org
    --format vcf
    --force_overwrite
    --everything
    --compress "gunzip -c"

This means that you will also need the human cache and reference sequence available. See `VEP Documentation <http://useast.ensembl.org/info/docs/>`_ for more info.

Future improvements may seek to allow tweaking of parameters using a config file. If you wish to modify this function to
in the meantime, please ensure that --hgvs is used, as this is used for validation purposes in the scripts that are
provided with this package.

Optimizing VEP
++++++++++++++

While not a topic specific to this package, I would like to point out a few adjustments that substantially speed up
VEP annotation. These changes can make an enormous different in the runtime.

 * Download relevant cache (27) and a .fasta file to use ``--cache``
 * Use ``--host useastdb.ensembl.org`` (USA users)
 * use ``--fork 4``
 * Convert the cache using tabix (see `Databases and Caches <http://useast.ensembl.org/info/docs/tools/vep/script/vep_cache.html>`_ for more info)

Unfortunately ``--hgvs`` (required for validation) requires internet access, so some database connection must be made. Specifying
the US mirror as the host (as specified above) greatly speeds up runtime because of this.

.. warning::
    Failing to optimize your VEP installation will result in prohibitively long execution time.


Remapping HGVS with VEP
+++++++++++++++++++++++

Note that it is possible to use HGVS formatted variants as input to VEP. At the time this package was developed, this was
incredibly slow. For this reason, I have used the third-party python module (`HGVS <https://github.com/counsyl/hgvs>`_) to
convert variants to VCF format prior to annotation.

This package is very fast and produced very comparable results to those of VEP and other available tools. This tool is also
useful for stand-alone HGVS to VCF (or vice versa) conversion. The leiden.remapping module provides functions for remapping.