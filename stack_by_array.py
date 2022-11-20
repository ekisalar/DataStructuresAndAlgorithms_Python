class Node:
    value = None
    next_node = None

    def __init__(self, value):
        self.value = value
        self.next_node = None


class Stack:
    data = []

    def __init__(self):
        self.data = []

    def peek(self):
        return self.data[len(self.data) - 1]

    def push(self, value):
        self.data.append(value)

    def pop(self):
        self.data.pop()

    def print(self) -> []:
        print(self.data)

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
