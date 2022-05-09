import os
import sys

SP_TICKER_URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
id = 'constituents'
DATA_URL = "https://finance.yahoo.com/quote/"

last_field = '1y Target Est'

path = 'SP_Constituents_Data/'
# sys.path.append(path)
storage_path = os.path.join(path, 'storage/')
ticker_storage_path = os.path.join(storage_path, 'Tickers/')
ticker_urls_file_path = 'ticker_urls.json'

ticker_path = os.path.join(path, ticker_urls_file_path)