import json

import scrapy

from tutorial.spiders.util.utils import construct_url

gender = 'women'


class CategorySpider(scrapy.Spider):
    name = 'category'

    def parse(self, response):
        pass

    def start_requests(self):
        url = construct_url(3, gender)
        yield scrapy.Request(url=url, callback=self.lvl2_parse)

    def lvl2_parse(self, response):
        response = json.loads(response.body_as_unicode())
        for root in response['root_tree']:
            cate_id = root['id_catalog_category']
            label = root['name']
            url_key = root['url_key']
            url = root['category_urls'][gender]
            depth = root['depth']
            yield {
                "label": label,
                "value": "",
                "category_id": cate_id,
                "url_key": url_key,
                "url": url,
                "depth": depth
            }
            yield scrapy.Request(url=construct_url(cate_id), callback=self.lvl3_parse)

    def lvl3_parse(self, response):
        response = json.loads(response.body_as_unicode())
        for category in response['category_tree']['children']:
            cate_id = category['id_catalog_category']
            label = category['name']
            url_key = category['url_key']
            url = category['category_urls'][gender]
            depth = category['depth']
            yield {
                "label": label,
                "value": "",
                "category_id": cate_id,
                "url_key": url_key,
                "url": url,
                "depth": depth
            }
            yield scrapy.Request(url=construct_url(cate_id), callback=self.lvl4_parse)

    def lvl4_parse(self, response):
        response = json.loads(response.body_as_unicode())
        for parent_category in response['category_tree']['children']:
            if parent_category['children']:
                cate_id = parent_category['id_catalog_category']
                label = parent_category['name']
                url_key = parent_category['url_key']
                url = parent_category['category_urls'][gender]
                depth = parent_category['depth']
                child_list = []
                for category in parent_category['children']:
                    child_list.append({
                        "label": category['name'],
                        "value": "",
                        "category_id": category['id_catalog_category'],
                        "url_key": category['url_key'],
                        "url": category['category_urls'][gender],
                        "depth": category['depth']
                    })
                yield {
                    "label": label,
                    "value": "",
                    "category_id": cate_id,
                    "url_key": url_key,
                    "url": url,
                    "depth": depth,
                    "children": child_list
                }
