##this folder documents the process of cleaning and processing the excel file containing the variants classified by ENIGMA

####ENIGMA excel files located at raw_files:

raw_files/ENIGMA_for_BRCAsite_9.21.2015.xlsx

raw_files/ENIGMA_SubmissionClinVar_2016-05-31_ncbi.xlsx

1. open raw_files/ENIGMA_for_BRCAsite_9.21.2015.xlsx with google spreadsheet, go to the "Variant" tab, select file -> download as -> Tab-separated values (tsv, .current sheet), rename and move downloaded file to raw_files/ENIGMA_variants_batch1_09_21_2015.tsv

2. repeat step 1 for file raw_files/ENIGMA_SubmissionClinVar_2016-05-31_ncbi.xlsx, open with google spreadsheet, go to variant tab, download as tsv file to raw_files/ENIGMA_variants_batch2_05_31_2016.tsv. However, here are three extra changes:

    rename column "Alternate designations" to "BIC Nomenclature"
    
    rename column "Official allele name" to "Abbrev AA change"
    
    remove last column "Replaces ClinVarAccessions"

3. set up virtualenv to run enigma-processing.py:

    `virtualenv env`

    `source env/bin/activat`

    `cd env`

    install pyhgvs library from counsyl, make sure pip version >= 8.1.2  

    `pip install pip --upgrade`

    `git clone https://github.com/counsyl/hgvs.git`

    `cd hgvs`

    `python setup.py install` 

    pip install rest of the requirements:

    `pip install -r requirement.txt`

4. under the new virtualenv, run `python enigma-processing.py`, the output file is saved as output/ENIMGA_last_updated_05-21-2016.tsv, ready to be used in variant merging.
 
