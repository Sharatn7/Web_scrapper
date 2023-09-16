import requests
import csv
from bs4 import BeautifulSoup

URL = ['https://www.amazon.in/s?k=bags&page=',
       '&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_']
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

# f = open("products.csv", "w", encoding='utf-8', newline='')
# headers = "Name, Price, Rating, Number of Reviews, Prd URL\n"
# f.write(headers)

with open('products.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Price", "Rating",
                    "Number of Reviews", "Prd URL"])

for page in range(1, 20):

    print("Page Number =", page)

    r = requests.get(URL[0]+str(page)+URL[1]+str(page), headers=HEADERS)
    soup = BeautifulSoup(r.content, 'lxml')
    links = soup.find_all("div", attrs={
                          'class': 's-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border'})

    for link in links:
        name = link.find("span", attrs={
            'class': 'a-size-medium a-color-base a-text-normal'}).string if link.find("span", attrs={'class': 'a-size-medium a-color-base a-text-normal'}) is not None else "No Name"
        print("Product Name =", name)

        price = link.find("span", attrs={
            'class': 'a-price-whole'}).string if link.find("span", attrs={'class': 'a-price-whole'}) is not None else "No Price"
        print("Product Price =", price)

        rating = link.find("span", attrs={
            'class': 'a-icon-alt'}).string if link.find("span", attrs={'class': 'a-icon-alt'}) is not None else "No Rating"
        print("Product Rating =", rating)

        review_count = link.find("span", attrs={
            'class': 'a-size-base s-underline-text'}).string if link.find("span", attrs={'class': 'a-size-base s-underline-text'}) is not None else "No Review Count"
        print("Number of Product Reviews =", review_count)

        prd_url = link.find("a", attrs={
                            'class': 'a-link-normal s-no-outline'})
        print("Product URL =", "https://www.amazon.in" + prd_url.get('href'))

        writer.writerow([name, price, rating, review_count, prd_url])
        # writer.writerow(name + "," +
        #         price + "," +
        #         rating + "," +
        #         review_count + "," +
        #         prd_url +
        #         "\n")

        print()
    # f.close()
