from static_scrape import StaticScrape
import os
from config import storage_path, id
import sys
print(sys.path)

class TickerScraper:
    def __init__(self, index):
        self.index = index
        self.scraper = StaticScrape(self.index)

    def get_tickers(self):
        if self.index == 's&p500':
            return self.sp500()
    
    def sp500(self):
        response = self.scraper.get_response()
        if not response:
            return
        soup = self.scraper.make_soup(response.text)
        const_table = self.scraper.find_table_by_id(soup, id)
        rows = const_table.find_all('tr')
        tickers = []
        for row in rows:
            data = row.find_all('td')
            ticker = []
            for i in range(len(data)):
                item = data[i].text.strip()
                if i == 0:
                    if '.' in item:
                        print(f'"." in {item}')
                        item = item.replace(".", "-")
                ticker.append(item)
                if i == 1:
                    ticker = tuple(ticker)
                    tickers.append(ticker)
                    break
        return tickers

    def scrape_and_save(self):
        tickers = self.get_tickers()
        if not tickers:
            print('No Tickers')
            return
        file_name = f'{self.index}_tickers.txt'
        file_path = os.path.join(storage_path, file_name)
        with open(file_path, 'w') as f:
            for ticker in tickers:
                f.writelines(' - '.join(ticker))
                f.writelines('\n')

if __name__ == '__main__':
    sp_scraper = TickerScraper('s&p500')
    sp_scraper.scrape_and_save()


