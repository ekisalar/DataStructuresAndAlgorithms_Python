class Node:
    value = None
    next_node = None

    def __init__(self, _value=None, _next_node=None):
        self.value = _value
        self.next_node = _next_node


class Data:
    None


class LinkedList:
    data = Data
    length = 0

    def __init__(self, value):
        self.data.header = Node(value, None)
        self.data.tail = self.data.header
        self.length += 1

    def append(self, value):
        new_node = Node(value, None)
        self.data.tail.next_node = new_node
        self.data.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value, self.data.header)
        self.data.header = new_node
        self.length += 1

    def print_values(self):
        counter = 0
        array = []
        current_node = self.data.header
        while counter < self.length:
            array.append(current_node.value)
            current_node = current_node.next_node
            counter += 1
        print(array)

    def traverse(self, index):
        counter = 0
        current_node = self.data.header
        if index <= 0:
            return current_node
        if index > self.length:
            return self.data.tail
        while counter < index:
            current_node = current_node.next_node
            counter += 1
        return current_node
