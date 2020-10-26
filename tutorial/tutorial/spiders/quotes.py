import scrapy


# class QuotesSpider(scrapy.Spider):
#     name = 'quotes'
#     allowed_domains = ['http://quotes.toscrape.com/page/1/']
#     start_urls = ['http://http://quotes.toscrape.com/page/1//']

#     def parse(self, response):
#         pass



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
        print('Entrou no parse')
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')