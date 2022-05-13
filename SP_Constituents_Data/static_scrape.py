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
            print(f'Requesting URL: {self.url}')
            response = requests.get(self.url, timeout=10)
            print('Got response...')
        except requests.exceptions.Timeout:
            count = 0
            while True:
                try:
                    print(f'Requesting URL: {self.url} again...')
                    response = requests.get(self.url)
                    print('Got response...')
                    break
                except requests.exceptions.Timeout:
                    if count == 5:
                        print(f'{count} retries. Exiting...')
                        break
                    count += 1
        except requests.exceptions.HTTPError as e:
            print(str(e))
            print(f'Error while making get request for URL: {self.url}')
            return None
        
        try:
            assert(response.status_code == 200)
        except:
            print('Response status code not 200')
            print(response.status_code)
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
    
    @staticmethod
    def find_tables(soup):
        try:
            tables = soup.find_all('table')
            return tables
        except Exception as e:
            print(str(e))
            print(f'Error while finding tables')
            return None

    @staticmethod
    def find_table_head(table):
        try:
            table_head = table.find('thead')
            return table_head
        except Exception as e:
            print(str(e))
            print('No head found')
            return None
    
    @staticmethod
    def get_rows(table):
        try:
            rows = table.find_all('tr')
            return rows
        except Exception as e:
            print(str(e))
            print('No rows')
            return None
    
    @staticmethod
    def find_header_row(table):
        try:
            rows = StaticScrape.get_rows(table)
            # print(rows)
            headings = [[headers for headers in row.find_all('th') if headers]
                                 for row in rows]
            headings = [heading for heading in headings if heading]
            return headings[-1]
        except Exception as e:
            print(str(e))
            print('No header rows')
            return None
    
    @staticmethod
    def find_data_rows(table):
        try:
            rows = StaticScrape.get_rows(table)
            data = [[data_rows for data_rows in row.find_all('td') if data_rows]
                               for row in rows]
            data = [data_row for data_row in data if data_row]
            return data
        except Exception as e:
            print(str(e))
            print('No data rows')
            return None