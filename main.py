from queue_by_linked_list import Queue

queue = Queue()

queue.enqueue("Jack")
queue.enqueue("Jones")
queue.enqueue("James")
queue.enqueue("Jany")
queue.print()
print(queue.peek().value)
queue.dequeue()
queue.print()
print(queue.peek().value)

