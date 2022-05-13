import os
from static_scrape import StaticScrape
from yahoo_scraper import YahooScraper
from config import storage_path
import datetime
import csv
import pandas as pd

# url = "https://finance.yahoo.com/quote/BBWI?p=BBWI"
# scraper = YahooScraper()
# scraper.set_url(url)
# data = scraper.get_data()

# file_name = 'sample.csv'
# file_path = os.path.join(storage_path, file_name)

# if not os.path.exists(file_path):
#     headers = list(data.keys())
#     with open(file_path, 'w', newline='\n') as f:
#         writer = csv.writer(f, lineterminator='\n')
#         writer.writerow(headers)

# values = list(data.values())
# with open(file_path, 'a', newline='\n') as f:
#     writer = csv.writer(f, lineterminator='\n')
#     writer.writerow(values)

url = "https://webscraper.io/test-sites/tables"
scraper = StaticScrape()
scraper.set_url(url)
response = scraper.get_response()
soup = scraper.make_soup(response.text)
tables = scraper.find_tables(soup)
# print(tables)

header_val = {}
for table in tables:
    headers = []
    values = []
    head = scraper.find_table_head(table)
    if head is None:
        # print(table)
        header_rows = scraper.find_header_row(table)
        
    else:
        header_rows = scraper.find_header_row(head)

    data_rows = scraper.find_data_rows(table)
    for row in data_rows:
        for key, value in zip(header_rows, row):
            if key.text in header_val:
                header_val[key.text].append(value.text)
            else:
                header_val[key.text] = [value.text]
    print('--------------------------------------')
print(header_val)