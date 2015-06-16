from setuptools import setup
setup(
    name='leiden',
    version='1.0.0',
    packages=['leiden'],
    scripts=['bin/extract_data.py', 'bin/generate_annotated_vcf.py', 'bin/validate_annotated_vcfs.py', 'bin/run_all.py'],
    url='https://github.com/andrewhill157/leiden',
    license='MIT License',
    author='Andrew Hill',
    author_email='andrewhill157@gmail.com',
    description='A set of tools for extracting, remapping, and validating variants from the Leiden Open Variation Databases (LOVD)',
    install_requires=['nose', 'hgvs', 'pygr', 'beautifulsoup4']
)
