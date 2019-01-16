import scrapy

class QuotesSpider(scrapy.Spider):
    name = "passwords"

    def start_requests(self):
        start_urls = [
            'https://foro.putalocura.com/threads/hilo-de-passwords-2-0.77820/page-2',
        ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'passwords-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)