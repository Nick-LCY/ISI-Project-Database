import scrapy

from tutorial.spiders.util.utils import construct_url

gender = 'men'


class ProductSpider(scrapy.Spider):
    name = 'product'

    def parse(self, response):
        pass

    def start_requests(self):
        url = construct_url(3, gender)
        yield scrapy.Request(url=url, callback=self.parse)
