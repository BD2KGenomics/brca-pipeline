import subprocess
import platform


def annotate_vep(input_file, output_file):
    """
    Annotate VCF file with Variant Effect Predictor.

    Args:
        input_file (str): input VCF file path
        output_file (str): output VCF file path (VEP annotation added to file).

    """
    # TODO - can use a config file to specify parameters, but have not gotten to work yet
    command = ['variant_effect_predictor.pl',
               '--vcf',
               '--cache',
               '--fork 4',
               '--host useastdb.ensembl.org',
               '--format vcf',
               '--force_overwrite',
               '--everything',
               '--input_file', input_file,
               '--output_file', output_file]

    if platform.system() == 'Darwin':
        command.append("--compress")
        command.append("gunzip -c")

    command = ' '.join(command)

    pipe = subprocess.Popen(command, shell=True)
    pipe.communicate()[0]