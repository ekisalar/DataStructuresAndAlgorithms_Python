class Node:
    value = None
    next_node = None

    def __init__(self, value):
        self.value = value
        self.next_node = None


class Stack:
    top = None
    bottom = None
    length = 0

    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            holding_pointer = self.top
            self.top = new_node
            self.top.next_node = holding_pointer
        self.length += 1
        self.print()

    def pop(self):
        if self.length == 0:
            return
        elif self.length == 1:
            self.top = None
            self.bottom = None
        else:
            self.top = self.top.next_node
        self.length -= 1
        self.print()

    def print(self) -> []:
        array = []
        if self.length < 1:
            return None
        current_node = self.top
        counter = 0
        while counter < self.length:
            array.append(current_node.value)
            current_node = current_node.next_node
            counter += 1
        return print(array)

# stack_by_linked_list = Stack()
# stack_by_linked_list.push(5)
# stack_by_linked_list.push(10)
# stack_by_linked_list.push(15)
# stack_by_linked_list.push(20)
# stack_by_linked_list.push(25)
# stack_by_linked_list.push(30)
# stack_by_linked_list.push(35)
# stack_by_linked_list.pop()
# stack_by_linked_list.pop()
# stack_by_linked_list.pop()
# stack_by_linked_list.pop()
# stack_by_linked_list.pop()
# stack_by_linked_list.pop()
# stack_by_linked_list.pop()
