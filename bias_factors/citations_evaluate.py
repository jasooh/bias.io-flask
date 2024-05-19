import news_api
import requests
from bs4 import BeautifulSoup
import re

# Example scoring criteria
source_quality_scores = {
    'journal': 10,
    'book': 8,
    'website': 5,
    'blog': 2,
    # Add more source types and their scores as needed
}

#urls = news_api.get_search_results()

def fetch_article_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch article content. Status code: {response.status_code}")

def extract_main_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs = soup.find_all('p')
    main_content = ' '.join([p.get_text() for p in paragraphs])
    return main_content

def extract_bibliography(text):
    # Assuming bibliography section starts with "References" or similar
    bibliography = []
    pattern = re.compile(r'(References|Bibliography)(.*?)(?=\n\n|\Z)', re.S)
    match = pattern.search(text)
    if match:
        references_text = match.group(2).strip()
        bibliography = references_text.split('\n')
    return bibliography

def extract_intext_citations(text):
    # Assuming in-text citations are in the format (Author, Year)
    citations = re.findall(r'\(([^)]+, \d{4})\)', text)
    return citations

def evaluate_bibliography(bibliography):
    score = 0
    for ref in bibliography:
        # Simplified source type detection
        if 'journal' in ref.lower():
            score += source_quality_scores['journal']
        elif 'book' in ref.lower():
            score += source_quality_scores['book']
        elif 'http' in ref.lower():
            score += source_quality_scores['website']
        elif 'blog' in ref.lower():
            score += source_quality_scores['blog']
        else:
            score += 1  # Default minimal score for unrecognized source types
    return score

def evaluate_intext_citations(citations, bibliography):
    score = 0
    for citation in citations:
        # Simplified matching: check if citation string is in any bibliography entry
        if any(citation.split(',')[0] in ref for ref in bibliography):
            score += 5  # Arbitrary score for matched citations
    return score

def evaluate_article(url):
    try:
        html_content = fetch_article_content(url)
        main_content = extract_main_content(html_content)
        bibliography = extract_bibliography(main_content)
        intext_citations = extract_intext_citations(main_content)
        
        bibliography_score = evaluate_bibliography(bibliography)
        intext_citation_score = evaluate_intext_citations(intext_citations, bibliography)
        
        total_score = bibliography_score + intext_citation_score
        return total_score
    except Exception as e:
        print(f"Error evaluating article: {e}")
        return 0

