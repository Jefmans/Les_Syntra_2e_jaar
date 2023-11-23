import requests
from bs4 import BeautifulSoup
from datetime import datetime

DOMAIN = 'https://www.jobat.be'

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
    # for nr in range (97, 123):
    for nr in range (97, 98):
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

    # print(all_urls)
    # print('---------------')

    return all_urls

def pagination_jobs(key, base_url):
    functie_titel = base_url.replace('https://www.jobat.be/nl/jobs/functietitels/', '')
    print(f'Started scraping Jobs for {functie_titel}')
    all_urls = set()
    page_nr = 1
    while True:
        print(f"scraping page {page_nr}")
        url = f"{base_url}?pagenum={page_nr}"
        print(url)
        response = requests.get(url, headers=headers)
        # print(response.status_code)
        # print(response.url)
        if len(response.history) > 0:
            if response.history[0].status_code == 301:
                break
        all_urls = all_urls.union(get_jobs_from_overview_function(response))

        page_nr += 1
    # print(all_urls)
    return {key : all_urls}


def detail_page(key_word, url):
    # url = 'https://www.jobat.be/nl/jobs/alarmtechnieker-regio-sint-truiden/job_3037133'
    url = 'https://www.jobat.be/nl/jobs/technieker-alarmsystemen-op-de-baan/job_3155163'
    r = requests.get(url, headers=headers)
    print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    job_detail = soup.find('div', 'jobDetails-content')
    job_title = job_detail.find('h1', 'jobTitle').text.strip()
    company_li = job_detail.find('li', 'jobCard-company')
    company_url = company_li.find('a')['href']
    company_name = company_li.find('a').span.span.text
    
    try: 
        email = job_detail.find('span', 'track-other-email').find('a', 'hidden').text
        print(email)
    except:
        email = None


    print('job title :' , job_title)
    print('Company name : ', company_name )
    print('Company url : ', company_url)
    

    

if __name__  == "__main__":
    # functie_titels_urls = functietitels_pages()
    functie_titels_urls = [{'account consultant': '/nl/jobs/functietitels/account-consultant'}]
    job_urls = set()
    for url_dict in functie_titels_urls:
        for key, value in url_dict.items():
            job_urls_per_functie_titel = pagination_jobs(key, DOMAIN+value)
            # print(job_urls_per_functie_titel)
            job_urls = job_urls.add(job_urls_per_functie_titel)
        
    # print(job_urls)

    for job_dict in job_urls:
        for key_word, url_list in job_dict:
            for url in url_list:
                detail_page(key_word, url)
