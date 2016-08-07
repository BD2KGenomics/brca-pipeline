##this folder documents the process of cleaning and processing the excel file containing the variants classified by ENIGMA

####ENIGMA excel files located at raw_files:

raw_files/ENIGMA_for_BRCAsite_9.21.2015.xlsx

raw_files/ENIGMA_SubmissionClinVar_2016-05-31_ncbi.xlsx

1. open excel file with google spreadsheet, go to the "Variant" tab, select file -> download as -> Tab-separated values (tsv, .current sheet), rename and move downloaded file to raw_files/ENIGMA_variants_batch1_9_21_2015.tsv

2. repeat step 1 for any new excel files ENIGMA sent us. Save file as raw_files/ENIGMA_variants_batch<fill in batch>_<fill in date>.tsv

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

4. 
