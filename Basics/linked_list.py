class Node:
    value = None
    next_node = None

    def __init__(self, _value=None, _next_node=None):
        self.value = _value
        self.next_node = _next_node


class Data:
    tail = None
    head = None


class LinkedList:
    data = Data
    length = 0

    def __init__(self, value):
        self.data.head = Node(value, None)
        self.data.tail = self.data.head
        self.length += 1

    def append(self, value):
        new_node = Node(value, None)
        self.data.tail.next_node = new_node
        self.data.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value, self.data.head)
        self.data.head = new_node
        self.length += 1

    def print_values(self):
        counter = 0
        array = []
        current_node = self.data.head
        while counter < self.length:
            array.append(current_node.value)
            current_node = current_node.next_node
            counter += 1
        print(array)

    def insert(self, index: int, value):
        if index >= self.length:
            return self.append(value)
        previous_node = self.traverse(index - 1)
        previous_node.next_node = Node(value, previous_node.next_node)
        self.length += 1

    def remove(self, index: int):
        previous_node = self.traverse(index - 1)
        previous_node.next_node = previous_node.next_node.next_node
        self.length -= 1

    def traverse(self, index: int) -> Node:
        counter = 0
        current_node = self.data.head
        if index <= 0:
            return current_node
        if index >= self.length:
            return self.data.tail
        while counter < index:
            current_node = current_node.next_node
            counter += 1
        return current_node

    # Interview question
    # Reverse the linked list
    # [5, 45, 23, 17, 56] ->
    # [56, 17, 23, 45, 5]

    def reverse(self) -> []:
        if self.data.head.next_node is None:
            return self.data.head

        first = self.data.head
        self.data.tail = self.data.head
        second = first.next_node
        while second is not None:
            temp = second.next_node
            second.next_node = first
            first = second
            second = temp
        self.data.tail.next_node = None
        self.data.head = first
        return self.print_values()


# linkedList = LinkedList(25)
# linkedList.append(35)
# linkedList.append(45)
# linkedList.prepend(15)
# linkedList.print_values()
# linkedList.insert(1, 20)
# linkedList.print_values()
# linkedList.remove(2)
# linkedList.print_values()
# print("finished")

# linkedList = LinkedList(5)
# linkedList.append(10)
# linkedList.append(15)
# linkedList.append(20)
# linkedList.append(25)
# linkedList.append(30)
# linkedList.print_values()
# linkedList.reverse()
