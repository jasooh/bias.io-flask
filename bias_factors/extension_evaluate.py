import news_api
from urllib.parse import urlparse

"""
edu, gov, com, org, net, mil = credible
Anything else = not as credible
xyz, info, top, biz, work, club, click, .gq, .cf, .ml, .tk, review, stream, download, loan = poor credibility
"""

tld_credibility_scores = {
    'com': 10,
    'org': 9,
    'net': 8,
    'edu': 10,
    'gov': 10,
    'io': 7,
    'co': 6,
    'info': 5,
    'biz': 4,
    'xyz': 3,
    'top': 2,
    'site': 1,
}

#urls = news_api.get_search_results()

def get_url_extension(url):
    """
    Extracts the top-level domain (TLD) from a given URL.

    Args:
        url (str): The URL from which to extract the TLD.

    Returns:
        str: The TLD of the URL.
    """
    try:
        # Parse the URL
        parsed_url = urlparse(url)
        # Extract the hostname
        hostname = parsed_url.hostname
        if hostname:
            # Split the hostname by dots and get the last part as the extension
            extension = hostname.split('.')[-1]
            return extension
        else:
            return None
    except Exception as e:
        print(f"Error parsing URL {url}: {e}")
        return None

#def collect_url_extensions(urls)

def get_credibility_score(tld):
    return tld_credibility_scores.get(tld, 0)

def evaluate_urls(urls):
    url_scores = []
    for url in urls:
        tld = get_url_extension(url)
        if tld:
            score = get_credibility_score(tld)
        else:
            score = 0
        url_scores.append((url, score))
    return url_scores
