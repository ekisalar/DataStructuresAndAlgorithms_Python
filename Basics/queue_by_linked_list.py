class Node:
    value = None
    next_node = None

    def __init__(self, value):
        self.value = value
        self.next_node = None


class Queue:
    first = None
    last = None
    length = 0

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first

    def dequeue(self):
        if self.first is None:
            return
        if self.first == self.last:
            self.last = None
        else:
            self.first = self.first.next_node
        self.length -= 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.last is None:
            self.first = new_node
            self.last = new_node
        else:
            holding_pointer = self.last
            self.last = Node(value)
            holding_pointer.next_node = self.last
        self.length += 1

    def print(self) -> []:
        array = []
        if self.length < 1:
            return None
        current_node = self.first
        counter = 0
        while counter < self.length:
            array.append(current_node.value)
            current_node = current_node.next_node
            counter += 1
        return print(array)


# queue = Queue()
#
# queue.enqueue("Jack")
# queue.enqueue("Jones")
# queue.enqueue("James")
# queue.enqueue("Jany")
# queue.print()
# print(queue.peek().value)
# queue.dequeue()
# queue.print()
# print(queue.peek().value)
