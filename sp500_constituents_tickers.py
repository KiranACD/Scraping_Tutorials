import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

def get_response(url):
    try:
        response = requests.get(url)
    except Exception as e:
        print(str(e))
        print(f'Error while making get request for URL: {url}')
        return None
    
    try:
        assert(response.status_code == 200)
    except:
        print('Response status code not 200')
        return None
    
    return response

def make_soup(html_text):
    try:
        soup = BeautifulSoup(html_text, features='html.parser')
        return soup
    except Exception as e:
        print(str(e))
        print('Error while making soup')
        return None

def find_table_by_id(soup, id):
    try:
        table = soup.find('table', {'id':id})
        return table
    except Exception as e:
        print(str(e))
        print(f'Error while finding table by id: {id}')
        return None


def scrape_tickers(url, id = None):
    response = get_response(url)
    if not response:
        return
    soup = make_soup(response.text)
    const_table = find_table_by_id(soup, id)
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
        
    # print(const_table)
    # print(len(const_table.contents))

tickers = scrape_tickers(url, 'constituents')
print(len(tickers))
