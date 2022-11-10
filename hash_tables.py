# My custom has table
# It generates custom hash code address modulus to hash table size
# Set function save key and value pairs to generated hash code address index
# Get function get the entered key's value from bucket which place in hashcode address

# Example
# myHashTable = HashTable(3) --> Create size 3 hash table
# myHashTable.set('grapes', 10000)
# myHashTable.set('apples', 10000)
# myHashTable.set('bananas', 10000)
# myHashTable.set('carrot', 10000)
# print(myHashTable.get('apples'))

class HashTable:
    data = [["grapes", 10000], ["apples", 5000]]

    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key):
        hashcode = 0
        i = 0
        while i < len(key):
            hashcode = (hashcode + ord(key[i]) * i) % len(self.data)
            i += 1
        return hashcode

    def set(self, key, value):
        address = self._hash(key)
        print("address", address)
        if self.data[address] is None:
            self.data[address] = []
        self.data[address].append([key, value])
        print(self.data)

    def get(self, key):
        hashcode = self._hash(key)
        for item in self.data[hashcode]:
            if item[0] == key:
                return item
