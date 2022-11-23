import json

from binary_search_tree import BinarySearchTree

# binary_search_tree = BinarySearchTree()
# binary_search_tree.insert(1000)
# binary_search_tree.insert(1500)
# binary_search_tree.insert(500)
# binary_search_tree.insert(550)
# binary_search_tree.insert(450)
# binary_search_tree.insert(1550)
# binary_search_tree.insert(1450)
# print("finish")
# looked_up_node = binary_search_tree.lookup(1550)
# print(looked_up_node)


#         9
#    4        20
# 1     6  15    170
binary_search_tree = BinarySearchTree()
binary_search_tree.insert(9)
binary_search_tree.insert(4)
binary_search_tree.insert(20)
binary_search_tree.insert(1)
binary_search_tree.insert(6)
binary_search_tree.insert(15)
binary_search_tree.insert(170)
[previous, current] = binary_search_tree.lookup(20)
json_data = json.dumps(binary_search_tree.data, default=lambda o: o.__dict__, indent=4)
print(json_data)
