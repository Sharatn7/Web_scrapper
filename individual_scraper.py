import requests
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

prd = requests.get("https://www.amazon.in/Urban-Tribe-Laptop-Backpack-Havana/dp/B01LXNNFDF/ref=sr_1_1_sspa?crid=2M096C61O4MLT&keywords=bags&qid=1675312860&sprefix=ba%2Caps%2C283&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&smid=A385M0TPSNV7VS&th=1", headers=HEADERS)
soup = BeautifulSoup(prd.content, 'lxml')

# details = soup.find_all(
#     "table", attrs={'class': 'a-keyvalue prodDetTable'})
# print("Description =", get_desc(soup))

# desc = soup.find_all(
#     "div", attrs={'class': 'a-section a-spacing-medium a-spacing-top-small'})
# prddesc = desc.find_all("span", attrs={'class': 'a-list-item'})
# print("* Product Description =", prddesc)

details = soup.find(
    "ul", attrs={'class': "a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list"})
count = 0
for detail in details:
    print(detail.find("span").string)
    # asin = details.find("li", attrs={'id': 'SalesRank'}).string
    # print("ASIN =", details.find("span", attrs={'class': ''}).string)

# manufacturer = details.find(
#     "td", attrs={'class': 'a-size-base prodDetAttrValue'}).string
# print("Manufacturer =", manufacturer)
