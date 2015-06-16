from nose.tools import assert_equals
from nose.tools import assert_raises
from . import utilities


def test_correct_hgvs_parentheses():
    # Basic notation with no parentheses
    input = 'c.4120A>T'
    result = 'c.4120A>T'
    assert_equals(utilities.correct_hgvs_parentheses(input), result)


def test_correct_hgvs_parentheses_with_parentheses():
    # Notation with enclosing parentheses
    input = 'c.(4120A>T)'
    result = 'c.4120A>T'
    assert_equals(utilities.correct_hgvs_parentheses(input), result)


def test_correct_hgvs_parentheses_with_brackets():
    # Use of brackets instead of parentheses
    input = 'c.[4120A>T]'
    result = 'c.4120A>T'
    assert_equals(utilities.correct_hgvs_parentheses(input), result)


def test_correct_hgvs_parentheses_with_p_dot():
    input = 'p.(4120A>T)'
    result = 'p.4120A>T'
    assert_equals(utilities.correct_hgvs_parentheses(input), result)


def test_correct_hgvs_parentheses_with_parentheses_notation():
    input = 'c.(4120A>T(8_20))'
    result = 'c.4120A>T(8_20)'
    assert_equals(utilities.correct_hgvs_parentheses(input), result)




def test_get_pmid():
    # Typical PubMed URL
    input = 'http://www.ncbi.nlm.nih.gov/pubmed/19562689'
    result = '19562689'
    assert_equals(utilities.get_pmid(input), result)

    # Early PubMed URL with shorter ID
    input = 'http://www.ncbi.nlm.nih.gov/pubmed/1592'
    result = '1592'
    assert_equals(utilities.get_pmid(input), result)

    # PMID is below the 4-digit minimum, should raise exception
    input = 'http://www.ncbi.nlm.nih.gov/pubmed/34'
    assert_raises(ValueError, utilities.get_pmid, input)

    # No PMID present, should raise exception
    input = 'http://www.ncbi.nlm.nih.gov/pubmed/'
    assert_raises(ValueError, utilities.get_pmid, input)


def test_get_omimid():
    # Typical OMIM URL
    input = 'http://www.omim.org/entry/102610#0001'
    result = '102610#0001'
    assert_equals(utilities.get_omimid(input), result)

    # Shortened, but valid, OMIM URL
    input = 'http://www.omim.org/entry/0#0'
    result = '0#0'
    assert_equals(utilities.get_omimid(input), result)

    # Invalid OMIM URL - no digits after #
    input = 'http://www.omim.org/entry/102610#'
    assert_raises(ValueError, utilities.get_omimid, input)

    # Invalid OMIM URL - no digits before #
    input = 'http://www.omim.org/entry/#102610'
    assert_raises(ValueError, utilities.get_omimid, input)

    # Invalid OMIM URL - no #
    input = 'http://www.omim.org/entry/102610'
    assert_raises(ValueError, utilities.get_omimid, input)

    # Invalid OMIM URL - no digits
    input = 'http://www.omim.org/entry/'
    assert_raises(ValueError, utilities.get_omimid, input)


def test_remove_times_reported():
    # Basic test case
    input = 'c.5235A>G (Reported 3 Times)'
    result = 'c.5235A>G'
    assert_equals(utilities.remove_times_reported(input), result)

    # Basic test case with more digits in times reported
    input = 'c.5235A>G (Reported 403 Times)'
    result = 'c.5235A>G'
    assert_equals(utilities.remove_times_reported(input), result)

    # Alternate position for target text
    input = '(Reported 403 Times) c.5235A>G'
    result = 'c.5235A>G'
    assert_equals(utilities.remove_times_reported(input), result)

    # Comparison is not case sensitive
    input = 'c.5235A>G (rePoRted 403 times)'
    result = 'c.5235A>G'
    assert_equals(utilities.remove_times_reported(input), result)

    # Should return unchanged without altering white-space
    input = ' c.5235A>G '
    result = ' c.5235A>G '
    assert_equals(utilities.remove_times_reported(input), result)


def test_find_string_index():
    # Basic test, should return first instance of strings appearing twice
    input = ['test', 'other', 'next', 'unit', 'other']
    result = 1
    assert_equals(utilities.find_string_index(input, 'other'), result)

    # Comparisons should not be case or white-space sensitive
    input = ['Test ', 'OtHeR ', ' nExt ', 'unit']
    result = 1
    assert_equals(utilities.find_string_index(input, 'other'), result)

    result = 2
    assert_equals(utilities.find_string_index(input, 'next '), result)

    # Comparisons should find substrings
    input = ['Word now', 'Word next', 'next', 'unit']
    result = 0
    assert_equals(utilities.find_string_index(input, 'Word'), result)

    # Return -1 if search string is not found
    input = ['test', 'other', 'next', 'unit', 'other']
    result = -1
    assert_equals(utilities.find_string_index(input, 'not in list'), result)

    # Return -1 if list is empty
    input = []
    result = -1
    assert_equals(utilities.find_string_index(input, 'target'), result)


def test_swap():
    # Basic example
    input = [1, 2, 3, 4, 5]
    result = [5, 2, 3, 4, 1]
    assert_equals(utilities.swap(input, 0, 4), result)

    # Swap element with itself
    input = [1, 2, 3, 4, 5]
    result = [1, 2, 3, 4, 5]
    assert_equals(utilities.swap(input, 3, 3), result)


def test_get_page_html():
    #TODO not sure what test would be appropriate here
    pass


def test_deep_copy():
    # Simple list, copy should match original
    input = [1, 2, 3, 4]
    result = utilities.deep_copy(input)
    assert_equals(result, input)

    # Changing one of the two should not change the other
    input[0] = 0
    assert_equals(result, [1,2,3,4])

    # List of lists, copy should match original
    input = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    result = utilities.deep_copy(input)
    assert_equals(result, input)

    # Changing an element in the inner list in one of the two should not change the other
    input[0][0] = 0
    assert_equals(result, [[1, 2, 3], [1, 2, 3], [1, 2, 3]])


