# -*- coding: utf-8 -*-
#!/usr/bin/env python

import argparse
import os
import pandas as pd
from leiden import annotate_vcf, vcf
from leiden.remapping import VariantRemapper

COLUMN_DELIMITER = '\t'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Produce an annotated VCF from raw LOVD output files. Requires that a copy'
                                                 'of variant_effect_predictor is on PATH with cache 27 and 28 installed and'
                                                 'the Downstream plugin installed.')

    group = parser.add_argument('-f', '--file_list',  help='File containing names of input raw LOVD output files to be annotated.')

    args = parser.parse_args()

    with open(args.file_list, 'r') as f:
        file_list = [x.split() for x in f]
    
    rm = VariantRemapper()

    for file in file_list:
        print 'file: ', file[0]
        base_file_name = os.path.splitext(file[0])[0]
        annotation_input_file = base_file_name + '_HGVS.temp'
        output_file = base_file_name + '.vcf'

        # Clean LOVD data for VCF
        lovd_file = pd.read_csv(file[0], sep=COLUMN_DELIMITER)
        lovd_file = vcf.remove_malformed_fields(lovd_file)

        # Output VCF variants for annotation
        #column_list = ['effect', 'dna_change','dna_change_genomic', 'rna_change', 'protein_change', 'haplotype', 'functionalanalysis_technique', 'functionalanalysis_result', 'exon', 'published_as', 'db_id', 'vip', 'variant_remarks', 'reference', 'dbsnp_id', 'genetic_origin', 'segregation', 'frequency', 're_site', 'methylation', 'owner']        
        column_list = []
        if 'BRCA1' in base_file_name:
            column_list = ['exon','dna_change','dna_change_bic','protein_change','posterior_p','iarc_class','observational_reference','prior_p_reference','missense_analysis_prior_p','splicing_prior_p','combined_prior_p','segregation_lr','pathology_lr','sum_family_lr','co_occurrence_lr','product_of_lrs','brca1_db_id']
        elif 'BRCA2' in base_file_name:
            column_list = ['exon','dna_change','dna_change_bic','protein_change','posterior_p','iarc_class','observational_reference','prior_p_reference','missense_analysis_prior_p','splicing_prior_p','combined_prior_p','segregation_lr','pathology_lr','sum_family_lr','co_occurrence_lr','product_of_lrs']

        print 'column_list: ', column_list
        print 'lovd_file.columns: ', lovd_file.columns        

        vcf_format = vcf.convert_to_vcf_format(lovd_file[column_list], rm, 'dna_change', column_list)
        vcf_column_order = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO']

        ##with open(annotation_input_file, 'w') as f:
        with open(output_file, 'w') as f:
            ## vcf.get_vcf_info_header(lovd_file[column_list], 'LOVD', 'Data from LOVD'),
            ##vcf_header = ['##fileformat=VCFv4.0', '##source=LOVD','##refernce=GRCh37', '##INFO=<ID=dna_change,Number=.,Type=String,Description="Description of variant at DNA level, based on a coding DNA reference sequence (following HGVS recommendations); e.g. c.123C>T, c.123_145del, c.123_126dup.">', '##INFO=<ID=dna_change_genomic,Number=.,Type=String,Description="Description of variant at DNA level, based on the genomic DNA reference sequence (following HGVS recommendations); e.g. g.12345678C>T, g.12345678_12345890del, g.12345678_12345890dup.">','##INFO=<ID=rna_change,Number=.,Type=String,Description="Description of variant at RNA level (following HGVS recommendations). e.g. r.123c>u, r.? = unknown, r.(?) = RNA not analysed but probably transcribed copy of DNA variant, r.spl? = RNA not analysed but variant probably affects splicing, r.(spl?) = RNA not analysed but variant may affect splicing, r.0? = change expected to abolish transcription.">','##INFO=<ID=protein_change,Number=.,Type=String,Description="Description of variant at protein level (following HGVS recommendations). e.g. p.(Arg345Pro) = change predicted from DNA (RNA not analysed), p.Arg345Pro = change derived from RNA analysis, p.? = unknown effect, p.0? = probably no protein produced.">','##INFO=<ID=haplotype,Number=.,Type=String,Description="Haplotype on which variant was found.">','##INFO=<ID=functionalanalysis_technique,Number=.,Type=String,Description="Functional analysis technique(s).">','##INFO=<ID=functionalanalysis_result,Number=.,Type=String,Description="Result of functional analysis.">','##INFO=<ID=exon,Number=.,Type=String,Description="Number of exon/intron containing variant; 2 = exon 2, 12i = intron 12, 2i_7i = exons 3 to 7, 8i_9 = border intron 8/exon 9.">','##INFO=<ID=effect,Number=.,Type=String,Description="The variants affect on a proteins function, in the format Reported/Curator concluded; [+] indicating the variant affects function, [+?] probably affects function, [-] does not affect function, [-?] probably does not affect function, [?] effect unknown, [.] effect not classified.">','##INFO=<ID=published_as,Number=.,Type=String,Description="Listed only when different from DNA change; variant as reported originally (e.g. 521delT). Variants seen in animal models, tested in vitro, predicted from RNA analysis, etc. are described between brackets like c.(456C>G)">','##INFO=<ID=db_id,Number=.,Type=String,Description="Database ID of variant, grouping multiple observations of the same variant together, starting with the HGNC gene symbol, followed by an underscore (_) and a six digit number (e.g. DMD_012345). _000000 is used for variants where DNA was not analysed (change predicted from RNA analysis), variants seen in animal models or variants not seen in humans but functionally tested in vitro.">','##INFO=<ID=vip,Number=.,Type=String,Description="Variant VIP-status was requested for matchmaking - need collaboration(s) to crack the case - please contact the submitter/curator. NOTE: to get VIP status ask the curator.">','##INFO=<ID=variant_remarks,Number=.,Type=String,Description="Remarks regarding variant described, e.g. germline mosaicism in mother, 345 kb deletion, muscle RNA analysed, not in 200 control chromosomes tested, on founder haplotype, etc.">','##INFO=<ID=reference,Number=.,Type=String,Description="publication describing the variant submitted, incl. links to OMIM, PubMed or other source, e.g. den Dunnen ASHG2003 P2346.">','##INFO=<ID=dbsnp_id,Number=.,Type=String,Description="The dbSNP ID.">','##INFO=<ID=genetic_origin,Number=.,Type=String,Description="Origin of variant; unknown, germline (inherited), somatic, de novo, from parental disomy (maternal or paternal) or in vitro (cloned) when tested for functional consequences. All options:([Unknown], [Germline (inherited)], [Somatic], [De novo], [Uniparental disomy], [Uniparental disomy, maternal allele], [Uniparental disomy, paternal allele], [In vitro (cloned)], or [Not applicable])">','##INFO=<ID=segregation,Number=.,Type=String,Description="Indicates whether the variant segregates with the phenotype (yes), does not segregate with the phenotype (no) or segregation is unknown (?). All options: [? = unknown], [yes = segregates with phenotype], [no = does not segregate with phenotype], [- = not applicable]">','##INFO=<ID=frequency,Number=.,Type=String,Description="Frequency in which the variant was found; e.g 5/760 chromosomes (in 5 of 760 chromosomes tested), 1/33 patients (in 1 of 33 patients analysed in study), 0.05 controls (in 5% of control cases tested).">','##INFO=<ID=re_site,Number=.,Type=String,Description="Restriction enzyme recognition site created (+) or destroyed (-); e.g. BglII+, BamHI-.">','##INFO=<ID=methylation,Number=.,Type=String,Description="Result of methylation test; GOM (gain of methylation), LOM (loss of methylation), 30% (30% methylated). NOTE: when several tests were done mention the method as well (e.g. MS-PCR 75%).">','#' + '\t'.join(vcf_column_order)]
            vcf_header = ['##fileformat=VCFv4.0', '##source=exLOVD','##refernce=GRCh37',
                          '##INFO=<ID=exon,Number=.,Type=String,Description="Standard BRCA1 (or BRCA2) exon numbering.">',
                          '##INFO=<ID=dna_change,Number=.,Type=String,Description="Sequence variant name in HGVS cDNA sequence based nomenclature.">',
                          '##INFO=<ID=dna_change_bic,Number=.,Type=String,Description="Sequence variant name in older BIC nomenclature.">',
                          '##INFO=<ID=protein_change,Number=.,Type=String,Description="Sequence variant name in HGVS protein amino acid sequence based nomenclature. Predicted effect of change on protein (usually without experimental proof!): [?]=unknown ; [(0)]=change expected to abolish translation ; [?fs]=frame shift, but observed phenotype does not fit with prediction (for instance less severe phenotype (BMD) observed, more severe phenotype (DMD) expected) ; [?no fs]=frame shift, but observed phenotype does not fit with prediction (for instance more severe phenotype (DMD) observed, less severe phenotype (BMD) expected) ; [del]=causes deletion ; [fs]=causes frame shift ; [fs?]=effect on reading frame very likely (no experimental proof) ; [(fs?)]=might affect the reading frame (no experimental proof) ; [no fs]=does not cause frame shift ; [X]=stop codon (nonsense).">',
                          '##INFO=<ID=posterior_p,Number=.,Type=String,Description="Posterior probability in favor of pathogenicity.">',
                          '##INFO=<ID=iarc_class,Number=.,Type=String,Description="Qualitative classification in the 5-grade IARC classification scheme. Class Description:[5 - Definitely pathogenic],Probability of being pathogenic:[>0.99] ; Class Description:[4 - Likely pathogenic],Probability of being pathogenic:[0.95-0.99] ; Class Description:[3 - Uncertain],Probability of being pathogenic:[0.05-0.949] ; Class Description:[2 - Likely not pathogenic or of little clinical significance],Probability of being pathogenic:[0.001-0.049] ; Class Description:[1 - Not pathogenic or of no clinical significance],Probability of being pathogenic:[<0.001]">',  
                          '##INFO=<ID=observational_reference,Number=.,Type=String,Description="Literature source of observational data used in the integrated evaluation displayed here. [Goldgar et al., AJHG 75: 535-544, 2004.], [Tavtigian et al., Human Mutation 29: 1342-1354, 2008.], [Wu, K. et al., Cancer Research 65: 417-426, 2005.], [Tavtigian, S.V. et al., Journal of Medical Genetics 43: 295-305, 2006.], [Chenevix-Trench, G. et al., Cancer Research 66: 2019-2027, 2006.], [Spurdle AB et al., J Clin Oncol, 26: 1657-1663, 2008.], [Easton DF et al., Am J Hum Genet, 81: 873-883, 2007.], [Miki Y et al., Science, 266:66-71, 1994.], [Spearman AD et al., J Clin Oncol, 26:5393-5400, 2008.], [Sweet K et al., Breast Cancer Res Treat, 119:737-743, 2010.], [Lovelock PK et al., J Med Genet, 43:74-83, 2006.], [Osorio A et al., Hum Mutat, 28:477-485, 2007.], [Tischkowitz M et al., Eur J Hum Genet, 16:820-832, 2008.], [Walker LC et al., Human Mutation 31: E1484-E1505, 2010], [Whiley et al., Human Mutation 32: 678-687, 2011], [Domchek SM et al., Cancer Discov 3: 399-405 (2013).], [Thomassen M et al., Breast Cancer Res Treat. 2012 Apr;132(3):1009-23.], [Whiley PJ et al., PLoS One. 2014 Jan 28;9(1):e86836.]">',
                          '##INFO=<ID=prior_p_reference,Number=.,Type=String,Description="Literature source of the sequence analysis based prior probability in favor of pathogenicity used in the integrated evaluation displayed here. [Goldgar et al., AJHG 75: 535-544, 2004.], [Tavtigian et al., Human Mutation 29: 1342-1354, 2008.], [Wu, K. et al., Cancer Research 65: 417-426, 2005.], [Tavtigian, S.V. et al., Journal of Medical Genetics 43: 295-305, 2006.], [Chenevix-Trench, G. et al., Cancer Research 66: 2019-2027, 2006.], [Vallée et al., manuscript submitted, 2015]">',
                          '##INFO=<ID=missense_analysis_prior_p,Number=.,Type=String,Description="This prior probability estimate combines position in the protein with an Align-GVGD based evaluation of missense substitutions that fall in the proteins key functional domains.">',
                          '##INFO=<ID=splicing_prior_p,Number=.,Type=String,Description="This prior probability estimate evaluates the sequence variants probability to damage a splice donor, damage a splice acceptor, or create a de novo splice donor.">',
                          '##INFO=<ID=combined_prior_p,Number=.,Type=String,Description="The combined prior probability in favor of pathogenicity. is a combination of the missense analysis prior probability and the splicing analysis prior probability. Generally, it is the higher of the two sequence analysis-based prior probabilities.">',
                          '##INFO=<ID=segregation_lr,Number=.,Type=String,Description="The likelihood ratio based on segregation analysis.">',
                          '##INFO=<ID=pathology_lr,Number=.,Type=String,Description="The likelihood ratio based on tumor pathology and/ or tumor immunohistochemistry.">',
                          '##INFO=<ID=sum_family_lr,Number=.,Type=String,Description="The likelihood ratio based on an analysis of the severity of summary family histories of breast and/ or ovarian cancer.">',
                          '##INFO=<ID=co_occurrence_lr,Number=.,Type=String,Description="The likelihood ratio based on the frequency of co-occurrence between the variant of interest and clearly pathogenic variants in the same gene.">',
                          '##INFO=<ID=product_of_lrs,Number=.,Type=String,Description="The product of all of the likelihood ratios">',
                          '##INFO=<ID=brca1_db_id,Number=.,Type=String,Description="Database IDentifier.">',
                        '#' + '\t'.join(vcf_column_order)
            ]
            f.write('\n'.join(vcf_header) + '\n')

            vcf_format[vcf_column_order].to_csv(f, sep=COLUMN_DELIMITER, header=False, index=False)

        # Annotate with VEP
        ##annotate_vcf.annotate_vep(annotation_input_file, output_file)

        # Combine VEP VCF output with original LOVD data
        ##with open(output_file, 'r') as f:
        ##    header_lines = vcf.get_vcf_header_lines(f)

        ##cumulative_vcf = pd.read_csv(output_file, header=len(header_lines)-1, sep=COLUMN_DELIMITER)

        # Make sure only variants with both CSQ and LOVD tags are in INFO column (VEP can't annotate some)
        ##cumulative_vcf = cumulative_vcf[cumulative_vcf['INFO'].str.contains('CSQ') & cumulative_vcf['INFO'].str.contains('LOVD')]

        # Write final VCF
        ##with open(output_file, 'w') as f:
        ##    f.writelines('\n'.join(header_lines) + '\n')
        ##   cumulative_vcf.to_csv(f, header=False, index=False, sep=COLUMN_DELIMITER)

        ##os.remove(annotation_input_file)
        
        print ''
