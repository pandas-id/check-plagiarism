from bs4 import BeautifulSoup
import requests
from urllib.parse import urlencode, unquote

# def parse_search_result()

base_url = 'https://www.google.com/search'


def scrape_query_results(query: str) -> list[tuple[str, str]]:
    results = []

    param = {
        'q': query,
        'lg': 'en'
    }

    url = f'{base_url}?{urlencode(param)}'

    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    results_element = soup.find_all('h3')

    for element in results_element:
        title = element.text
        url = element.find_parent('a')['href']
        url = unquote(url.replace('/url?q=', '').split('&sa=')[0])

        results.append((title, url))

    return results


# scrape_query_results('Cara mendapatkan cookies facebook login')
