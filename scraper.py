import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    span_counter = 0
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    paragraphs = soup.findAll("p")

    for p in paragraphs:
        if p.find('span'):
            span_counter += 1
    return span_counter


def get_citations_needed_report(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    paragraphs = soup.findAll("p")

    # reports = []
    for p in paragraphs:
        if p.find('span'):
            print(p)
    # return reports




if __name__ == "__main__":
    print(get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico'))
    get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Mexico')

