import requests
from bs4 import BeautifulSoup
import json
from config import ticker_path
import sys
print(sys.path)

class StaticScrape:
    def __init__(self, index = None):
        self.index = index
    
    @property
    def url(self):
        try:
            return self._url
        except:
            if self.index:
                self.url_()
                return self._url
    
    def set_url(self, url):
        self._url = url
    
    def url_(self):
        with open(ticker_path) as file:
            urls = json.load(file)
            self._url = urls[self.index]

    def get_response(self):
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
    def find_table_by_id(soup, id):
        try:
            table = soup.find('table', {'id':id})
            return table
        except Exception as e:
            print(str(e))
            print(f'Error while finding table by id: {id}')
            return None