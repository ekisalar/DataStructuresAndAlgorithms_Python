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
            target_node = self.data
            previous_node = None
            while target_node is not None:
                if value > target_node.value:
                    # left direction
                    previous_node = target_node
                    target_node = target_node.right

                elif value < target_node.value:
                    # right direction
                    previous_node = target_node
                    target_node = target_node.left

            if value > previous_node.value:
                previous_node.right = new_node
            elif value < previous_node.value:
                previous_node.left = new_node

    def lookup(self, value):
        current_node = self.data
        level = 0
        while current_node is not None and current_node.value != value:
            level += 1
            if value > current_node.value:
                current_node = current_node.right
            elif value < current_node.value:
                current_node = current_node.left

        return f"{current_node.value} found at level {level}" if current_node is not None else "Not Found"

    # def traverse(self):
    #     tree = Node(self.data.value)
    #     tree.left = None if self.data.left is None else self.traverse(self.data.left)
    #     tree.right = None if self.data  .right is None else self.traverse(self.data.right)
    #     return tree
