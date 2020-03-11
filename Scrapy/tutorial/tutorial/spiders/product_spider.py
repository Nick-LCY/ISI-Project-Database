import json
from urllib.parse import quote

import scrapy


class ProductSpider(scrapy.Spider):
    name = 'product'

    def start_requests(self):
        url = 'https://www.zalora.com.hk/_c/v1/desktop/list_catalog_full?params='
        url += quote(str({
            'url': '/women/shoes/flip-flops',
            'q': '',
            'sort': 'popularity',
            'dir': 'desc',
            'offset': 0,
            'limit': 99,
            'category_id': [
                '385'
            ],
            'range': [],
            'occasion': [],
            'material_composition': [],
            'pattern': [],
            'campaign_categoryId': [],
            'color': [],
            'sizesystem': [],
            'brand': [],
            'age_group': [],
            'gender': [
                'women'
            ],
            'price': '',
            'normalized_sell_through': '',
            'segment': 'women',
            'special_price': False,
            'all_products': False,
            'new_products': False,
            'top_sellers': False,
            'catalogtype': 'Main',
            'campaign': '',
            'discount': '',
            'age': '',
            'mp': '',
            'or': '',
            'shipment_type': '',
            'exs': '',
            'lang': 'en',
            'is_brunei': False,
            'sort_formula': '',
            'rerank_formula': '',
            'search_suggest': False,
            'custom_filters': {
                'filter1': '',
                'filter2': '',
                'filter3': '',
                'filter4': ''
            },
            'elevate_ids': [],
            'user_id': '',
            'enable_visual_sort': True,
            'enable_filter_ads': True,
            'features': {
                'compact_catalog_desktop': False,
                'name_search': False,
                'solr7_support': True,
                'pick_for_you': False,
                'learn_to_sort_catalog': False
            },
            'onsite_filters': {},
            'user_query': '',
            'is_multiple_source': True
        }))
        url = url.replace('%27', '"')
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        file_obj = open('./data/product.sql', 'w')
        response = json.loads(response.body_as_unicode())
        for doc in response['response']['docs']:
            name = doc['meta']['name']
            category = 'A___'
            price = doc['meta']['price'].replace('HK$ ', '')
            thumbnail_location = doc['image']
            insert_statement = 'INSERT INTO product (name, category, price, out_of_stock, thumbnail_location) VALUES ("'
            data = name + '", "' + category + '", ' + price + ', 0, "' + thumbnail_location + '");\n'
            insert_statement += data
            file_obj.write(insert_statement)

        file_obj.close()
