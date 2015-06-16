import os
import re

import hgvs
import hgvs.utils
from pygr.seqdb import SequenceFileDB

class VariantRemapper:
    """
    Class containing functions for remapping of variants from HGVS to genomic coordinate notation.

    Attributes:
        genome (SequenceFileDB): reference sequence DB object

    """

    def __init__(self):
        """
        Initializes hg19 reference and reference transcripts
        """
	print(__file__)
	print()
	print()
	print()
        genome_path = os.path.join(os.path.dirname(__file__), 'resources', 'hg19.fa')
        refseq_path = os.path.join(os.path.dirname(__file__), 'resources', 'genes.refGene')
	print('genome_path: ', genome_path)
	print('refseq_path: ', refseq_path)
	
        # Read genome sequence using pygr.
        self.genome = SequenceFileDB(genome_path)

        # Read RefSeq transcripts into a python dict.
        with open(refseq_path) as infile:
            self.transcripts = hgvs.utils.read_transcripts(infile)

    def hgvs_to_vcf(self, hgvs_variant):
        """
        Converts a single variant provided in HGVS notation to genomic coordinate notation.

        See Counsyl's HGVS library for more information on acceptable input formats: https://github.com/counsyl/hgvs.

        Args:
            hgvs_variant (str): HGVS description of variant, such as NM_001100.3:c.137T>C.
                The portion prior to the colon is the refseqID used as the reference for the variant The portion after
                the colon is an HGVS-style description of the mutation (a SNP from T to C at location 137 in the example above.

        Returns:
            tuple of str: (chromosome_number, coordinate, ref, alt) in that order denoting the VCF notation of the variant

        """

        # Library requires string not unicode, ensure format is correct
        hgvs_variant = str(hgvs_variant)

        chromosome_number, coordinate, ref, alt = hgvs.parse_hgvs_name(hgvs_variant, self.genome, get_transcript=self._get_transcript)
        chromosome_number = re.match('chr(.+)', chromosome_number).group(1)
        coordinate = str(coordinate)

        return chromosome_number, coordinate, ref, alt

    def vcf_to_hgvs(self, reference_transcript, vcf_notation):
        """
        Converts a single VCF notation variant to HGVS notation relative to a given transcript.

        See Counsyl's HGVS library for more information on acceptable input formats: https://github.com/counsyl/hgvs.

        Args:
            reference_transcript (str): the refseq id of the reference transcript to use for HGVS notation
            vcf_notation (tuple of str): a tuple containing elements chromosome_number, coordinate, ref, and alt in that order

        Returns:
            str: hgvs notatation of variant in format reference_transcript:hgvs_description

        """

        chromosome_number, coordinate, ref, alt = vcf_notation
        coordinate = int(coordinate)

        transcript = self._get_transcript(reference_transcript)

        return hgvs.format_hgvs_name(chromosome_number, coordinate, ref, alt, self.genome, transcript)

    def _get_transcript(self, name):
        """
        Callback to provide reference transcript by its name

        Args:
            name (str): name of reference transcript

        Returns:
            line of information on transcript from resource file

        """
        return self.transcripts.get(name)
