import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0',
    'Referer' : 'https://www.google.com',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language' : 'nl-be, en;q=0.9, fr;q=0.8, en-US;q=0.7',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Sec-Fetch-Mode' : 'navigate',
    'Sec-Fetch-Site' : 'same-origin',
    'Sec-Fetch-Dest' : 'document',
    'Upgrade-Insecure-Requests' : '1'
}

domain ='https://www.immoweb.be'


def scrape_overview_page(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all('h2', 'card__title card--result__title')
    all_urls = set()
    for result in results:
        all_urls.add(result.a['href'])
    
    return all_urls
    