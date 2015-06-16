import requests


def get_page_html(page_url):
    """
    Returns the html describing the page at the specified URL.

    Args:
        page_url (str): URL to a specified website

    Returns:
        str: HTML describing the specified page

    Raises:
        ValueError: if requested URL not found
        IOError: if page could not be reached

    """

    response = requests.get(page_url)

    if response.status_code == 404:
        raise ValueError('Requested URL not found.')
    if response.status_code > 404:
        raise IOError('Requested URL not found. Status code: %d' % response.status_code)
    return response.text