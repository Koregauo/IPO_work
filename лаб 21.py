import requests
from bs4 import BeautifulSoup
import csv

HOST = "www.belinvestbank.by"
url = "https://www.belinvestbank.by/exchange-rates/courses-tab-group1?town=%D0%9C%D0%B8%D0%BD%D1%81%D0%BA&operation=3&showList=map&display=office"
user_agent = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; hu-HU; rv:1.7.8) Gecko/20050511 Firefox/1.0.4'}
r = requests.get(url, headers = user_agent)
#print(r)

soup = BeautifulSoup(r.text,"html.parser")
#print(soup)

items = soup.find_all("tr")
items.pop(0)
#print(items)

courses = []
for item in items:
    _item = item.find_all("td")
    print(_item)
#    courses.append({
#        'naim': _item[0].find("span",class_="text").get_text(),
#        'curAmount': _item[1].get_text(),
#        'curs': _item[2].get_text().strip()
#    })
#print(courses)

with open('curs.csv.lab','w') as file:
    writer = csv.DictWriter(
        file,
        fieldnames = ['naim','curAmount','curs'],
        delimiter = ';',
        lineterminator = '\r',
        quoting = csv.QUOTE_MINIMAL
    )
    writer.writeheader()
    for elem in courses:
        writer.writerow(elem)
        #ответ по примеру из лекции