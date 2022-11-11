from hash_tables import HashTable
from two_sums import TwoSum

myHashTable = HashTable(3)  # --> Create size 3 hash table
myHashTable.set('grapes', 10000)
myHashTable.set('apples', 10000)
myHashTable.set('bananas', 10000)
myHashTable.set('carrot', 10000)
print(myHashTable.get('apples'))
print("keys", myHashTable.keys())
