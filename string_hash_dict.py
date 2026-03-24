from string_hash import simple_string_hash


class StringHashDictionary:
    def __init__(self):
        self.data = {}

    def add(self, key):
        self.data[key] = simple_string_hash(key)

    def find(self, key):
        return self.data.get(key)
