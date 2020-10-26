import json
import re

import jsonlines
import scrapy
import urllib.request

from bs4 import BeautifulSoup

from utils.constants import STATES, URL 


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            print(f'Vou ler a url {url}')
            yield scrapy.Request(url=url, callback=self.parse)
            print(f'Terminei de rodar a url {url}')

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


def main():
    for state in STATES: 
        values = urllib.parse.urlencode({'UF': state})
        values = values.encode('ascii')

        urlResponse = urllib.request.urlopen(URL,values)

        html = urlResponse.read().decode('ISO-8859-1')

        soup = BeautifulSoup(html, 'lxml')

        regularExpression = r"(?:<td.*?>)(.*?)(?:</td>)"
        
        result = re.findall(regularExpression,html)
        
        
        """
        how I want the dict: 

        {"uf": "ac", "cep": "50000-000", "locals": [{"recife": "50000-000"}, {"olinda": "50000-0000"}]  }
        
        state_dict = {}
        
        i = 0
        
        for row in result:
            if i == 0:
                state_dict["UF"] = row
            elif i == 1:
                state_dict["faixa_cep"] = row
            print(row)
            i += 1 """
        
        to_json = json.dumps(result)
        
        print("\n========= " + state + " information =========\n" )
        print(to_json)


if __name__ == '__main__':
    main()