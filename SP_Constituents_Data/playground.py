import os
from yahoo_scraper import YahooScraper
from config import storage_path
import datetime
import csv

url = "https://finance.yahoo.com/quote/MMM?p=MMM"
scraper = YahooScraper()
scraper.set_url(url)
data = scraper.get_data()

file_name = 'sample.csv'
file_path = os.path.join(storage_path, file_name)

if not os.path.exists(file_path):
    headers = list(data.keys())
    with open(file_path, 'w', newline='\n') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(headers)

values = list(data.values())
with open(file_path, 'a', newline='\n') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(values)