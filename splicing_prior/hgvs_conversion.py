"""
convert VCF genomic coordinate format to HGVS format and back
Note: currently only supporting genomic assembly version HG38 (GRCh38)
"""

import pyhgvs
import pyhgvs.utils as hgvs_utils
from pygr.seqdb import SequenceFileDB


HG38 = SequenceFileDB("/cluster/home/mollyzhang/reference_genome/hg38/hg38.fa")

with open('../resources/refseq/hg38.BRCA.refGene.txt') as infile:
    transcripts = hgvs_utils.read_transcripts(infile)

def get_transcript(name):
    return transcripts.get(name)

def VCF_to_HGVS(genome_coor):
    chrom, pos, refalt = genome_coor.replace("-", "").split(":")
    ref, alt = refalt.split(">")
    if chrom == "chr13":
        transcript = get_transcript("NM_000059")
    elif chrom == "chr17":
        transcript = get_trascript("NM_007294")
    else:
        raise Exception("chromsome name error")
    hgvs_name = pyhgvs.format_hgvs_name(chrom, pos, ref, alt, genome, transcript)
    return hgvs_name

