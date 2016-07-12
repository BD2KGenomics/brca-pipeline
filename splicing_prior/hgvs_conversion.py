"""
convert VCF genomic coordinate format to HGVS format and back
Note: currently only supporting genomic assembly version HG38 (GRCh38)
"""

import pyhgvs
import pyhgvs.utils as hgvs_utils
from pygr.seqdb import SequenceFileDB


HG38 = SequenceFileDB("/cluster/home/mollyzhang/reference_genome/hg38/hg38.fa")

with open('../resources/refseq/hg38.BRCA.refGene.txt') as infile:
    transcripts = pyhgvs_utils.read_transcripts(infile)

def get_transcript(name):
    return transcripts.get(name)

def VCF_to_HGVS(genome_coor):
    pass

