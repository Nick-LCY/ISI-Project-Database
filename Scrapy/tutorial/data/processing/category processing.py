import json


class NewCategory(object):
    def __init__(self, cate_id, label, url_key, url, depth):
        self.cate_id = cate_id
        self.label = label
        self.children = []
        self.value = ''
        self.url_segments = url.split('/')[1:]
        self.url_key = url_key
        self.depth = depth

    def to_string(self):
        string = '{"label": "' + self.label + '", "value": "' \
                 + self.value + '", "category_id": ' + str(self.cate_id) + ', ' \
                 + '"url": ' + str(self.url_segments).replace("'", '"') + ', "depth": ' + str(self.depth) \
                 + ', "children": ['
        if self.children:
            for child in self.children:
                string += child.to_string() + ', '
            string = string[0: -2]
        string += ']}'
        return string

    def to_cate_string(self):
        string = '{"label": "' + self.label + '", "value": "' \
                 + self.value + '", "children": ['

        if self.children:
            for child in self.children:
                string += child.to_cate_string() + ', '
            string = string[0: -2]
        string += ']}'
        return string


def add_value(parent, child):
    if not parent.children:
        child.value = parent.value[0:int(parent.value.find('_'))] + 'A___'
        child.value = child.value[0:4]
    else:
        last = parent.children[len(parent.children) - 1]
        if last.value.find('_') != -1:
            child.value = last.value[0:last.value.find('_') - 1] + str(
                chr(ord(last.value[last.value.find('_') - 1]) + 1)) + '____'
        else:
            child.value = last.value[0:-1] + str(
                chr(ord(last.value[-1]) + 1)) + '____'
        child.value = child.value[0:4]


with open('../row_category.json') as f:
    data = json.load(f)
record_list = []
for record in data:
    new = NewCategory(record['category_id'], record['label'], record['url_key'], record['url'], record['depth'])
    if 'children' in record:
        for lvl4 in record['children']:
            new.children.append(
                NewCategory(lvl4['category_id'], lvl4['label'], lvl4['url_key'], lvl4['url'], lvl4['depth']))
    record_list.append(new)

women = NewCategory(0, 'Women', 'women', '/women', 1)
women.value = 'A___'
men = NewCategory(0, 'Men', 'men', '/men', 1)
men.value = 'B___'
del_list = []
# lvl2
for cate in record_list:
    if len(cate.url_segments) == 2:
        if cate.url_segments[0] == 'men':
            add_value(men, cate)
            men.children.append(cate)
        else:
            add_value(women, cate)
            women.children.append(cate)
        del_list.append(cate)

for del_item in del_list:
    record_list.remove(del_item)
del_list = []

# lvl3
lvl2_category_ids = set()
for cate in record_list:
    for lvl2 in men.children:
        if (len(cate.url_segments) == 3) & (cate.url_segments[0] == 'men'):
            if lvl2.url_key == cate.url_segments[1]:
                if cate.cate_id in lvl2_category_ids:
                    if cate.children:
                        for redundant_lvl2 in men.children:
                            for redundant_lvl3 in redundant_lvl2.children:
                                if redundant_lvl3.cate_id == cate.cate_id:
                                    for lvl4 in cate.children:
                                        add_value(redundant_lvl3, lvl4)
                                        redundant_lvl3.children.append(lvl4)
                    del_list.append(cate)
                else:
                    add_value(lvl2, cate)
                    lvl2.children.append(cate)
                    lvl2_category_ids.add(cate.cate_id)
                    del_list.append(cate)
    for women_cate in women.children:
        if (len(cate.url_segments) == 3) & (cate.url_segments[0] == 'women'):
            if women_cate.url_key == cate.url_segments[1]:
                add_value(women_cate, cate)
                if cate.cate_id in lvl2_category_ids:
                    if cate.children:
                        for redundant_parent in women.children:
                            for redundant_one in redundant_parent.children:
                                if redundant_one.cate_id == cate.cate_id:
                                    for lvl4 in cate.children:
                                        add_value(redundant_one, lvl4)
                                        redundant_one.children.append(lvl4)
                    del_list.append(cate)
                else:
                    women_cate.children.append(cate)
                    lvl2_category_ids.add(cate.cate_id)
                    del_list.append(cate)

for del_item in del_list:
    record_list.remove(del_item)
del_list = []

file = open('../cate_id_value_mapping.json', 'w')
file.write('[')
file.write(men.to_string())
file.write(',')
file.write(women.to_string())
file.write(']')
file.close()

file = open('../processed_category.json', 'w')
file.write('[')
file.write(men.to_cate_string())
file.write(',')
file.write(women.to_cate_string())
file.write(']')
file.close()


