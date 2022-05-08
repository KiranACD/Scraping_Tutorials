import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AAPL?p=AAPL"
response = requests.get(url)
file_name = 'values.txt'


t = response.text

soup = BeautifulSoup(t, features='html.parser')

# tables = soup.find_all("tbody")
# for table in tables:
#     for table_row in table:
#         print(table_row.contents.text)
        # print('----------------------------------------')
# print(tables)
# print(table_rows[0].text)
# print(table_rows[0].td)

table_rows_fields = soup.find_all("td", class_="C($primaryColor) W(51%)")
table_rows_values = soup.find_all("td", class_="Ta(end) Fw(600) Lh(14px)")


with open('values.txt', 'w') as f:
    for field, value in zip(table_rows_fields, table_rows_values):  
        f.write(f'{field.text} - {value.text}')
        f.write('\n')
    

