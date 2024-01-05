from lib.html_parser import parse_html_document
from lib.similarity import cosine_similarity
from lib.google_parser import scrape_query_results
import multiprocessing
import requests
import requests.exceptions

# initialization
url = input('url: ')

resp = requests.get(url, allow_redirects=True)

data = parse_html_document(resp.text)
query = data['title']

print(f'title: {query}')

# documen yang akan dicari tingkat kesamaannya
query_document = data['body']

urls = scrape_query_results(query)
urls = [url[1] for url in urls]

def get_data(url: str):
    try:
        resp = requests.get(url, allow_redirects=True)
        return parse_html_document(resp.text)
    except requests.exceptions.SSLError:
        return None
    except requests.exceptions.ConnectionError:
        return None

def calculate_article_similarity(url: str):
    data = get_data(url)

    if data is None:
        return None

    title = data['title']
    document = data['body']

    sim = cosine_similarity(query_document, document)

    # print(url)
    # print(title)
    # print(round(sim * 100, 2))
    # print()

    return (url, title, sim)


def main():
    with multiprocessing.Pool() as pool:
        results = [ pool.apply_async(calculate_article_similarity, args=(url,)) for url in urls ]

        pool.close()
        pool.join()

        # dapatkan return value
        results = [ result.get() for result in results ]

        results = filter(lambda x: x != None, results)

        # urutkan tingkat similarity
        results = sorted(results, key=lambda x: x[2], reverse=True)

        for result in results:
            if result != None:
                url, title, sim = result
                print()
                print(url)
                print(title)
                print(round(sim * 100, 2))

if __name__ == "__main__":
    main()
