class Node:
    right = None
    left = None
    value = None

    def __init__(self, value=None):
        self.value = value


class BinarySearchTree:
    data = None

    def insert(self, value):
        new_node = Node(value)
        if self.data is None:
            self.data = new_node
            return
        else:
            current_node = self.data
            previous_node = None
            while current_node is not None:
                if value > current_node.value:
                    # left direction
                    previous_node = current_node
                    current_node = current_node.right

                elif value < current_node.value:
                    # right direction
                    previous_node = current_node
                    current_node = current_node.left

            if value > previous_node.value:
                previous_node.right = new_node
            elif value < previous_node.value:
                previous_node.left = new_node

    def lookup(self, value):
        current_node = self.data
        previous_node = None
        level = 0
        while current_node is not None and current_node.value != value:
            level += 1
            if value > current_node.value:
                previous_node = current_node
                current_node = current_node.right
            elif value < current_node.value:
                previous_node = current_node
                current_node = current_node.left
        return previous_node, current_node


## Not completed

# def remove(self, value):
#
#     [previous_node, node_to_remove] = self.lookup(value)
#     node_to_replace = None
#     if node_to_remove.right is not None:
#         if node_to_remove.right.left is not None:
#             node_to_replace = node_to_remove.right.left
#
#         else:
#             node_to_replace = node_to_remove.right
#         if previous_node.left == node_to_remove:
#             previous_node.left = node_to_replace
#         else:
#             previous_node.right = node_to_replace
#     elif node_to_remove.left is not None:
#         node_to_replace = node_to_remove.left
#
#
#     if previous_node.left == node_to_remove:
#         if node_to_replace is None:
#             previous_node.left
#
#     if previous_node.right == node_to_remove:
#
#
#     if node_to_replace is None:


# Example
#         9
#    4        20
# 1     6  15    170
# binary_search_tree = BinarySearchTree()
# binary_search_tree.insert(9)
# binary_search_tree.insert(4)
# binary_search_tree.insert(20)
# binary_search_tree.insert(1)
# binary_search_tree.insert(6)
# binary_search_tree.insert(15)
# binary_search_tree.insert(170)
# [previous, current] = binary_search_tree.lookup(20)
# json_data = json.dumps(current.data, default=lambda o: o.__dict__, indent=4)
# print(json_data)
