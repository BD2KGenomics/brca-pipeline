this folder contains scripts related splicing variant prediction

#####to use VCFSpliceAnnotator
1. download USeq at http://downloads.sourceforge.net/project/useq/USeq_8.9.6.zip?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fuseq%2F&ts=1467909346&use_mirror=tenet
2. java -Xmx10G -jar USeq_8.9.6/Apps/VCFSpliceAnnotator -r VCFSA_output/ -v VCFSA_input/vcfs/ClinVarBRCA1.vcf -f VCFSA_input/fasta_files/HG19_GRCh37/ -u VCFSA_input/hg19EnsemblTrans.ucsc -m VCFSA_input/splicemodels/ -h VCFSA_input/spliceHistograms.sjo


#####to use MaxEntScan
1. download MaxEntScan at http://genes.mit.edu/burgelab/maxent/download/fordownload.tar.gz
2. gunzip fordownload.tar.gz
3. tar -xvf fordownload.tar
4. 
perl score5.pl test5
perl score3.pl test3
