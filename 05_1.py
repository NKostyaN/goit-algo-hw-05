class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key, value):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            key_value = [key, value]
            for pair in self.table[key_hash]:
                if pair[0] == key and pair[1] == value:
                    self.table[key_hash].remove(key_value)


H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)
H.insert("kiwi", 25)

print("Before deletion:\n", H.table)

H.delete("kiwi", 25)

print("After deletion:\n", H.table)
