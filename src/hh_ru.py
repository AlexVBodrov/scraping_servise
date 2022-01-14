import requests
import codecs

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

url = 'https://hh.ru/search/vacancy?text=Python&items_on_page=500'

resp = requests.get(url, headers=headers)

h = codecs.open('work.html', 'w', 'utf-8')
h.write(str(resp.text))
h.close()