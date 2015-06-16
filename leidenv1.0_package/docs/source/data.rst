.. _data:

Data
====

I have included examples of the major data formats output from the scripts in this package.

Extracted Data
^^^^^^^^^^^^^^
The naming convention is <gene_name>.txt.

Contains original variant data as found on LOVD. Files are saved per gene by extract_data.py. See /data/ACTA1.txt

Annotated VCF Files
^^^^^^^^^^^^^^^^^^^
Naming convention is <gene_name>.vcf.

Contains original data in VCF format with Variant Effect Predictor annotation. Files are saved per input file by generate_annotated_vcf.py. See /data/ACTA1.vcf

Final VCF Files
^^^^^^^^^^^^^^^
This is the file format output by validate_annotated_vcfs.py. They are the VCF files that contains discordant and concordant variants respectively. See /data/lovd_discordant_variants.vcf
and /data/lovd_validated_variants.vcf.

