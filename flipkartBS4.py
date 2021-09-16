import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

descriptions = []
processors = []
ram = []
os = []
storage = []
inches = []
warranty = []
prices = []
ratings = []

pages = list(range(1, 24))
for page in pages:
    req = requests.get("https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_"
                       "OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_""QueryStore_OrganicAutoSuggest_1_2_na_na_na&as-pos="
                       "1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=3ce7332a-be81-4159-92b7-98f69e046507&as-"
                       "searchtext=la&page={}".format(page)).text
    soup = BeautifulSoup(req, 'html.parser')
    print(soup.prettify())
    desc = soup.find_all('div', class_='_4rR01T')
    #print(desc)
    for i in range(len(desc)):
        descriptions.append(desc[i].text)
    len(descriptions)
    commonclass = soup.find_all('li', class_='rgWa7D')
    #print(commonclass)
    for i in range(0, len(commonclass)):
        p = commonclass[i].text
        if ("Core" in p):
            processors.append(p)
        elif ("RAM" in p):
            ram.append(p)
        elif ("HDD" in p or "SSD" in p):
            storage.append(p)
        elif ("Operating" in p):
            os.append(p)
        elif ("Display" in p):
            inches.append(p)
        elif ("Warranty" in p):
            warranty.append(p)
    price = soup.find_all('div', class_="_30jeq3 _1_WHN1")
    for i in range(len(price)):
        prices.append(price[i].text)
    len(prices)
    rating = soup.find_all('div', class_="gUuXy-")
    for i in range(len(rating)):
        ratings.append(rating[i].text)
        len(ratings)

    d = (len(descriptions))
    print(d)
    p = (len(processors))
    print(p)
    r = (len(ram))
    print(r)
    o = (len(os))
    print(o)
    s = (len(storage))
    print(s)
    w = (len(warranty))
    print(w)
    i = (len(inches))
    print(i)
    pr = (len(prices))
    print(pr)
    ra = (len(ratings))
    print(ra)
    print("=======================================")
df = {'Description': descriptions[50], 'Processor': processors[50], 'RAM': ram[50], 'Operating System': os[slice(50)], 'Storage': storage[slice(50)], 'Display': inches[slice(50)], 'Warranty': warranty[slice(50)], 'Price': prices[slice(50), 'Ratings': ratings[slice(50)]]}
dataset = pd.DataFrame(data=df)
print(dataset)