import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AAPL?p=AAPL"
response = requests.get(url)
file_name = 'values.txt'
last_name = '1y Target Est'

soup = BeautifulSoup(response.text, features='html.parser')

table_rows = soup.find_all('tr')

names = []
values = []
name_values = {}

for row in table_rows:
    for j in range(len(row.contents)):
        if j == 0:
            name = row.contents[j].text
            names.append(name)
        elif j == 1:
            value = row.contents[j].text
            values.append(value)
    name_values[name] = value
    
    if name == last_name:
        break

print(name_values)