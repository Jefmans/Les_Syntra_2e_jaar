import requests
from bs4 import BeautifulSoup
from bier_utils import remove_digit_part, split_naam, Bier

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

url = "https://www.prikentik.be/bier"

r = requests.get(url, headers=headers)
# print(r.status_code)
soup = BeautifulSoup(r.text, 'html.parser')

products = soup.main.find('ol', 'product-items')
# products = soup.find('div', attrs={'class':'products-grid'})
# products = soup.find('div', 'products', 'wrapper')

# bieren = products.contents
bieren = products.find_all('li', 'product-item')
# bieren = products.findChildren('li', 'product-item')
# bieren = products.children
# print(bieren[0])

bieren_set = set()

for bier in bieren:
    bier_link = bier.find('a', "product-item-link")
    naam, vol_type = split_naam(bier_link.string)
    new_naam = remove_digit_part(naam)
    # print(new_naam, ' : ', vol_type)
    url = bier_link['href']    
    # print(url)
    bieren_set.add(Bier(new_naam, vol_type, url))

for bier in bieren_set:
    r = requests.get(bier.url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    prijs = float(soup.find('span', 'price').text[2:].replace(',', '.'))
    bier.set_prijs(prijs)

for bier in bieren_set:
    print(bier)

if __name__ == '__main__':
    bieren = scrape_product_page()
    for bier in bieren:
        scrape_detail_page_bier(bier)