import requests

url = "https://finance.yahoo.com/quote/AAPL?p=AAPL"

prop = "Previous Close"

r = requests.get(url)

print(r)
t = ''
if r.status_code == 200:
    t = r.text
    
if t:
    ind = t.index(prop)
    # Value that we want is going to be after this index
    price_text = t[ind:].split('</td>')[1].split('>')[-1]
    # price_text = price_text.split('')
    print(price_text)