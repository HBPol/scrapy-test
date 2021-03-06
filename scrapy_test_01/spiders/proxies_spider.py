import scrapy

class QuotesSpider(scrapy.Spider):
    name = "proxies"

    def start_requests(self):
        start_urls = [
            'http://quotes.toscrape.com/page/1/',
        ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'proxies-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)