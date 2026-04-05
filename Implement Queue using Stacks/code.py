class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, x: int) -> None:
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError
        val = self.top.value
        self.top = self.top.next
        self._size -= 1
        return val

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError
        return self.top.value

    def is_empty(self) -> bool:
        return self.top is None

    def size(self) -> int:
        return self._size


class MyQueue:
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def push(self, x: int) -> None:
        self.stack_1.push(x)

    def pop(self) -> int:
        if self.stack_2.is_empty():
            while not self.stack_1.is_empty():
                self.stack_2.push(self.stack_1.pop())

        return self.stack_2.pop()

    def peek(self) -> int:
        if self.stack_2.is_empty():
            while not self.stack_1.is_empty():
                self.stack_2.push(self.stack_1.pop())

        return self.stack_2.peek()

    def empty(self) -> bool:
        return self.stack_1.is_empty() and self.stack_2.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
