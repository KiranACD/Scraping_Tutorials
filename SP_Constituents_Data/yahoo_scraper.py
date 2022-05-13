from static_scrape import StaticScrape
from config import last_field
import datetime

class YahooScraper:
    def __init__(self):
        self.scraper = StaticScrape()

    def set_last_field(self):
        self.last_field = last_field

    def set_url(self, url):
        self.scraper.set_url(url)
    
    def get_response(self):
        response = self.scraper.get_response()
        return response
    
    def make_soup(self):
        response = self.get_response()
        if response is None:
            return None
        soup = self.scraper.make_soup(response.text)
        return soup
    
    def get_rows(self):
        soup = self.make_soup()
        if soup is None:
            return None
        rows = soup.find_all('tr')
        return rows
    
    def get_data(self):
        rows = self.get_rows()
        if not rows:
            print('Did not get rows')
            return
        name_values = {}
        name_values['datetime'] = datetime.datetime.now().replace(microsecond=0).strftime('%d-%m-%Y %H:%M:%S')
        print('got rows')
        for row in rows:
            for j in range(len(row.contents)):
                if j == 0:
                    name = row.contents[j].text
                elif j == 1:
                    value = row.contents[j].text
            name_values[name] = value
            
            if name == last_field:
                break
        return name_values


    

