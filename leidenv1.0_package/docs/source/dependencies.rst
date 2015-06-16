.. _dependencies:

Installation and Dependencies
=============================

Installation for General Use (No Development)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
While this project ideally could be installed using a default installation, some dependencies do not always install correctly.

In the next sections I will step through the installation process for the two finicky dependencies.

.. important::
    Install the dependencies below first and then install leiden.

Once these dependencies are installed, you can do any of the following:

Clone:

.. code-block:: bash

    git clone git@github.com:andrewhill157/leiden.git

Clone and Install from Source:

.. code-block:: bash

    git clone git@github.com:andrewhill157/leiden.git
    cd leiden
    python setup.py install leiden


All project dependencies are listed in requirements.txt. If you simply want to install the dependencies for the project
without installing the package itself run the command from the package root directory:

.. code-block:: bash

    pip install -r requirements.txt

If you want to contribute to the project via Github, please see the :ref:`contributing` page.

pygr
++++

pygr requires that you have bsddb3 and Berkeley DB installed. This can be installed using homebrew:

.. code-block:: bash

    brew install berkeley-db --without-java

# Note prefix to pip not required on Broad cluster
sudo BERKELEYDB_DIR=/usr/local/Cellar/berkeley-db/5.3.15/ pip install bsddb3

Once bbd3 and Berkeley DB are installed, you should be able to install pygr with pip install pygr. If there are still errors,
the following may correct the problem.

.. code-block:: bash

    export CFLAGS=-Qunused-arguments
    export CPPFLAGS=-Qunused-arguments
    pip install pygr

I have not encountered any additional problems installing pygr.

hgvs
++++
HGVS must be installed by cloning the Github repository and installing from source:

.. code-block:: bash

    git clone git@github.com:counsyl/hgvs.git
    cd hgvs
    python setup.py install
    cd ..
    rm -rf hgvs

I have not encountered any additional problems installing hgvs.

.. important::
    Unfortunately, this tool depends on a relatively large file that I cannot easily host on Github. This is normally housed
    in the folder /leiden/remapping/resources/. It is a human genome reference sequence (hg19.fa) I have temporarily hosted a
    copy at at: http://www.broadinstitute.org/~ahill. This file will need to decompressed using gunzip and placed in
    /leiden/remapping/resources/. The first time this package is used, two additional files will be generated (takes some time).
    Subsequent runs will not require this process to be repeated.

Other Errors
++++++++++++

I have also seen an error stating that pg_config executable could not be found. This seems to be an executable included
with PostgreSQL, which can be downloaded with homebrew, etc.:

.. code-block:: bash

    brew install postgresql

Variant Effect Predictor
++++++++++++++++++++++++

Variant Effect Predictor (VEP) is required to use generate_annotated_vcf.py and the annotate_vcf module. The downstream script validate_annotated_vcfs.py
depends on the annotations that VEP provides to perform validation. Since run_all.py calls these scripts, it also requires VEP. See :ref:`vep` for more info.

The extract_data.py and the other packages in leiden can be used without VEP.

.. important::
    VEP must be installed and on your path to generate and validate annotated VCF files.

Development Installation
^^^^^^^^^^^^^^^^^^^^^^^^

If you would like to extend or modify the existing code-base or scripts while still having the package installed,
you can install in editable or development mode. This differs slightly from the default installation mode.

The easiest way to do this is to install from cloned source.

.. code-block:: bash

    git clone git@github.com:andrewhill157/leiden.git
    cd leiden
    python setup.py develop

Either of these methods will make the leiden packages accessible by python, but allow you to edit and call the modified
source without re-installing the package. Note that the dependencies must still be installed according to instructions in
the Installation for General Use section.

If you want to contribute to the project via Github, please see the :ref:`contributing` page.