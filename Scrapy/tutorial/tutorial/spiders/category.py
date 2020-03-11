class Category(object):
    def __init__(self, value, label, children):
        self.value = value,
        self.label = label,
        self.children = children

    def to_result(self):
        result = {
            "value": self.value,
            "label": self.label,
            "children": []
        }

        for child in self.children:
            result['children'].append(child.to_result())
        return result

    def equal(self, cate2):
        return cate2.label == self.label
