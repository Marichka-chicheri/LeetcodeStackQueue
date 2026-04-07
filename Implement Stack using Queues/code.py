class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, x: int):
        new_node = Node(x)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
        self._size += 1

    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError
        val = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self._size -= 1
        return val

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError
        return self.head.value

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q2.enqueue(x)
        
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())
        
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.dequeue()

    def top(self) -> int:
        return self.q1.peek()

    def empty(self) -> bool:
        return self.q1.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
