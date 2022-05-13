import os
import csv
import time
import random
from ticker_iterator import Tickers
from static_scrape import StaticScrape
from config import DATA_URL, ticker_storage_path
from yahoo_scraper import YahooScraper

class ConstituentsData:

    def __init__(self, index):
        self.index = index
        self.tickers = Tickers(self.index)
        self.scraper = YahooScraper()
    
    def generate_url(self):
        for ticker in self.tickers:
            print(ticker)
            file_name = f'{ticker}.csv'
            self.file_path = os.path.join(ticker_storage_path, file_name)
            url = DATA_URL + f'{ticker}?p={ticker}'
            yield url

    def get_data(self):
        url_generator = self.generate_url()
        for url in url_generator:
            self.scraper.set_url(url)
            data_value = self.scraper.get_data()
            yield data_value

    def save(self):
        data_gen = self.get_data()
        for data in data_gen:
            if not data:
                print('Skipping...')
                print('-------------------------------------------')
                continue
            if not os.path.exists(self.file_path):
                headers = list(data.keys())
                with open(self.file_path, 'w', newline='\n') as f:
                    writer = csv.writer(f, lineterminator='\n')
                    writer.writerow(headers)
            values = list(data.values())
            with open(self.file_path, 'a', newline='\n') as f:
                writer = csv.writer(f, lineterminator='\n')
                writer.writerow(values)
            print('done')
            print('-------------------------------------------')

            time.sleep(random.randint(1, 2))

    def run(self):
        while True:
            self.save()

if __name__ == '__main__':
    store_data = ConstituentsData('s&p500')
    store_data.run()
    
    
