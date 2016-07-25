"""
convert VCF genomic coordinate format to HGVS format and back
Note: currently only supporting genomic assembly version HG38 (GRCh38)
"""

import pyhgvs
import pyhgvs.utils as hgvs_utils
from pygr.seqdb import SequenceFileDB


HG38 = SequenceFileDB("/cluster/home/mollyzhang/reference_genome/hg38/hg38.fa")
HG19 = SequenceFileDB("/cluster/home/mollyzhang/reference_genome/hg19/hg19.fa")
GENOME = {"hg38": HG38, "hg19": HG19}


with open('../resources/refseq/hg38.BRCA.refGene.txt') as infile:
    transcripts_hg38 = hgvs_utils.read_transcripts(infile)
with open('../resources/refseq/hg19.BRCA.refGene.txt') as infile:
    transcripts_hg19 = hgvs_utils.read_transcripts(infile)
TRANSCRIPTS = {"hg19": transcripts_hg19, "hg38": transcripts_hg38}



def get_transcript(name, version):
    return TRANSCRIPTS[version].get(name)

def VCF_to_HGVS(genome_coor, version="hg38"):
    chrom, pos, ref, alt = genome_coor
    if chrom == "chr13":
        transcript = get_transcript("NM_000059", version)
    elif chrom == "chr17":
        transcript = get_transcript("NM_007294", version)
    else:
        raise Exception("chromsome name error")
    hgvs_name = pyhgvs.format_hgvs_name(chrom, pos, ref, alt, GENOME[version], transcript)
    return hgvs_name

