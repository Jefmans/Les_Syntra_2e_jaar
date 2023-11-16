import requests
from bs4 import BeautifulSoup
from datetime import datetime

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

def functietitels_pages():
    all_urls = []
    for nr in range (97, 123):
        url = f"https://www.jobat.be/nl/jobs/functietitels/{chr(nr)}"
        r = requests.get(url, headers=headers)
        # print(url ,r.status_code)
        print(f"scraping links for {chr(nr)}")
        all_urls += get_functietitles_per_page(url)
    return all_urls

def get_functietitles_per_page(url):
    
    page_urls = []
    # url = f"https://www.jobat.be/nl/jobs/functietitels/a"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    functie_titels_li = soup.find_all('li', 'List-item')
    for functie_li in functie_titels_li:
        keyword = functie_li.find('span', 'List-text').text
        page_urls.append({keyword : functie_li.a['href']})
        
    return page_urls



def get_jobs_from_overview_function(response):
    all_urls = set()
    # url = f"https://www.jobat.be/nl/jobs/functietitels/alarmsystemen"

    soup = BeautifulSoup(response.text, 'html.parser')
    all_jobs = soup.find_all('h2', 'jobTitle')
    # print(all_jobs)
    for job in all_jobs:
        url = job.a['href']
        all_urls.add(url)

    return all_urls

def pagination_jobs():
    all_urls = set()
    page_nr = 1
    while True:
        print(f"scraping page {page_nr}")
        url = f"https://www.jobat.be/nl/jobs/functietitels/alarmsystemen?pagenum={page_nr}"
        response = requests.get(url, headers=headers)
        print(response.status_code)
        print(response.url)
        if len(response.history) > 0:
            if response.history[0].status_code == 301:
                break
        all_urls.union(get_jobs_from_overview_function(response))

        page_nr += 1
    return all_urls


def detail_page():
    pass

if __name__  == "__main__":
    # print(functietitels_pages())
    # print(get_functietitles_per_page())
    # get_jobs_from_overview_function()
    print(pagination_jobs())
