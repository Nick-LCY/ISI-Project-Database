import scrapy
from tutorial.spiders.category import Category


class CategorySpider(scrapy.Spider):
    name = "category"
    counter = 0
    name_list = ['women', 'men']

    def start_requests(self):
        urls = [
            'https://www.zalora.com.hk/women/',
            'https://www.zalora.com.hk/men/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        category = Category(None, None, [])
        category.label = self.name_list[self.counter]
        category.value = (chr(ord('A') + self.counter) + '____')[0:4]
        for link in response.css(
                'ul li.b-header__category-bar-text.prl.js-category-bar-text a.b-header__clickable::attr(href)'):

            sub_category = Category(None, None, [])
            sub_sub_category = Category(None, None, [])

            row_cat = link.get()
            index = row_cat.find('?')
            if index != -1:
                row_cat = row_cat[1:index - 1]
            else:
                row_cat = row_cat[1: -1]
            row_cat = row_cat.replace('/', '%')
            cat_list = row_cat.split('%')
            # yield {"wow": row_cat}

            length = len(cat_list)
            sub_category.label = cat_list[1]
            processing_sub_cate(category, sub_category)
            if length == 3:
                sub_sub_category.label = cat_list[2]
                for cate in category.children:
                    if cate.equal(sub_category):
                        processing_sub_cate(cate, sub_sub_category)

        self.counter += 1
        yield category.to_result()


def processing_sub_cate(parent: Category, child: Category):
    is_not_in = True
    for exist in parent.children:
        if exist.equal(child):
            is_not_in = False
    if is_not_in:
        if not parent.children:
            child.value = parent.value[0:int(parent.value.find('_'))] + 'A___'
            child.value = child.value[0:4]
        else:
            last = parent.children[len(parent.children) - 1]
            child.value = last.value[0:last.value.find('_') - 1] + str(
                chr(ord(last.value[last.value.find('_') - 1]) + 1)) + '____'
            child.value = child.value[0:4]
        parent.children.append(child)
