class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.count = 0
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.count += 1

        if self.count / self.size > 0.7:
            self.resize()

    def search(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for existing_key, value in bucket:
            if existing_key == key:
                return value
        return None

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (existing_key, value) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                self.count -= 1
                return value
        return None

    def resize(self):
        old_items = []
        for bucket in self.table:
            old_items.extend(bucket)

        self.size *= 2
        self.count = 0
        self.table = [[] for _ in range(self.size)]

        for key, value in old_items:
            self.insert(key, value)

    def __str__(self):
        lines = []
        for i, bucket in enumerate(self.table):
            lines.append(f"{i}: {bucket}")
        return "\n".join(lines)
