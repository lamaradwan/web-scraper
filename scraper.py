import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
    span_counter = 0
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    paragraphs = soup.findAll("p")

    for p in paragraphs:
        span = p.find('span')
        if span:
            if span.getText() == 'citation needed':
                span_counter += 1
    return span_counter


def get_citations_needed_report(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    paragraphs = soup.findAll("p")

    for p in paragraphs:
        span = p.find('span')
        if span:
            if span.getText() == 'citation needed':
                print(p.getText())


if __name__ == "__main__":
    print(get_citations_needed_count('https://en.wikipedia.org/wiki/Saudi_Arabia'))
    get_citations_needed_report('https://en.wikipedia.org/wiki/Saudi_Arabia')
