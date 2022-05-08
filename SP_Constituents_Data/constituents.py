import requests
from bs4 import BeautifulSoup
import os
import json
from config import storage_path, ticker_path, id

class TickerScraper:
    def __init__(self, index):
        self.index = index
    
    @property
    def url(self):
        try:
            return self._url
        except:
            self.url_()
            return self._url
    
    def url_(self):
        with open(ticker_path) as file:
            urls = json.load(file)
            self._url = urls[self.index]

    def get_response_(self):
        try:
            response = requests.get(self.url)
        except Exception as e:
            print(str(e))
            print(f'Error while making get request for URL: {self.url}')
            return None
        
        try:
            assert(response.status_code == 200)
        except:
            print('Response status code not 200')
            return None
    
        return response

    @staticmethod
    def make_soup(html_text):
        try:
            soup = BeautifulSoup(html_text, features='html.parser')
            return soup
        except Exception as e:
            print(str(e))
            print('Error while making soup')
            return None
    
    @staticmethod
    def find_table_by_id(soup):
        try:
            table = soup.find('table', {'id':id})
            return table
        except Exception as e:
            print(str(e))
            print(f'Error while finding table by id: {id}')
            return None

    def get_tickers(self):
        if self.index == 's&p500':
            return self.sp500()
    
    def sp500(self):
        response = self.get_response_()
        if not response:
            return
        soup = TickerScraper.make_soup(response.text)
        const_table = TickerScraper.find_table_by_id(soup)
        rows = const_table.find_all('tr')
        tickers = []
        for row in rows:
            data = row.find_all('td')
            ticker = []
            for i in range(len(data)):
                ticker.append(data[i].text.strip())
                if i == 1:
                    ticker = tuple(ticker)
                    tickers.append(ticker)
                    break
        return tickers

    def scrape_and_save(self):
        tickers = self.get_tickers()
        file_name = f'{self.index}_tickers.txt'
        file_path = os.path.join(storage_path, file_name)
        with open(file_path, 'w') as f:
            for ticker in tickers:
                f.write(ticker)
                f.write('\n')


