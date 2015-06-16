from nose.tools import assert_equals, assert_true, assert_false
from leiden import validation


#######################################################################################################################
# Tests for is_concordant
#######################################################################################################################
def test_is_concordant():
    protein_change_1 = 'Arg890Tyr'
    protein_change_2 = 'Arg890Tyr'

    assert_true(validation.is_concordant(protein_change_1, protein_change_2))


def test_is_concordant_with_different_coordinate():
    protein_change_1 = 'Arg890Tyr'
    protein_change_2 = 'Arg892Tyr'

    assert_false(validation.is_concordant(protein_change_1, protein_change_2))


def test_is_concordant_with_different_amino_acid():
    protein_change_1 = 'Arg890Tyr'
    protein_change_2 = 'Arg890Lys'

    assert_false(validation.is_concordant(protein_change_1, protein_change_2))


def test_is_concordant_with_different_case():
    protein_change_1 = 'Arg890Tyr'
    protein_change_2 = 'ARG890TYR'

    assert_true(validation.is_concordant(protein_change_1, protein_change_2))


def test_is_concordant_with_stop_codon_notation():
    protein_change_1 = 'Arg890Tyrfs*50'
    protein_change_2 = 'Arg890TyrfsX50'

    assert_true(validation.is_concordant(protein_change_1, protein_change_2))


def test_is_concordant_with_stop_codon_notation2():
    protein_change_1 = 'Arg890Tyrfs*50'
    protein_change_2 = 'Arg890TyrfsXaa50'

    assert_true(validation.is_concordant(protein_change_1, protein_change_2))


def test_is_concordant_with_stop_codon_notation3():
    protein_change_1 = 'Arg890Tyrfs*50'
    protein_change_2 = 'Arg890TyrfsTer50'

    assert_true(validation.is_concordant(protein_change_1, protein_change_2))


def test_is_concordant_with_transcript_id():
    protein_change_1 = 'NP_32562.3:Arg890Tyr'
    protein_change_2 = 'Arg890Tyr'

    assert_true(validation.is_concordant(protein_change_1, protein_change_2))


#######################################################################################################################
# Tests for normalize_protein_notation
#######################################################################################################################

# Indirectly tested by is_concordant tests

#######################################################################################################################
# Tests for get_ucsc_location_link
#######################################################################################################################
def test_get_ucsc_location_link_with_standard_interval():
    # Basic test to ensure URL is constructed correctly
    chromosome = '1'
    start_coordinate = '15613'
    end_coordinate = '52552'
    result = 'http://genome.ucsc.edu/cgi-bin/hgTracks?db=hg19&position=chr1%3A15613-52552'

    assert_equals(validation.get_ucsc_location_link(chromosome, start_coordinate, end_coordinate), result)


#######################################################################################################################
# Tests for remove_p_dot_notation
#######################################################################################################################
def test_remove_p_dot_notation_with_standard_notation():
    # Basic notation with no parentheses
    input = 'p.Gly47Arg'
    result = 'Gly47Arg'
    assert_equals(validation.remove_p_dot_notation(input), result)


def test_remove_p_dot_notation_with_parentheses():
    # Notation with enclosing parentheses
    input = 'p.(Lys5799Glu)'
    result = 'Lys5799Glu'
    assert_equals(validation.remove_p_dot_notation(input), result)


def test_remove_p_dot_notation_with_brackets():
    # Use of brackets instead of parentheses
    input = 'p.[Lys5799Glu]'
    result = 'Lys5799Glu'
    assert_equals(validation.remove_p_dot_notation(input), result)


def test_remove_p_dot_notation_with_missing_opening_parentheses():
    # Missing starting parentheses
    input = 'p.(Met563Lys'
    result = 'Met563Lys'
    assert_equals(validation.remove_p_dot_notation(input), result)


def test_remove_p_dot_notation_with_missing_closing_parentheses():
    # Missing closing parentheses
    input = 'p.Met563Lys)'
    result = 'Met563Lys'
    assert_equals(validation.remove_p_dot_notation(input), result)



