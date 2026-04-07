from collections import deque

class FrequencyLevel:
    def __init__(self, count):
        self.count = count
        self.items = deque()
        self.next = None

class FreqStack:
    def __init__(self):
        self.levels_head = None
        self.max_freq = 0

    def push(self, val: int) -> None:
        current_f = self._find_current_freq(val)
        new_f = current_f + 1
        
        target_level = self._get_or_create_level(new_f)
        
        target_level.items.append(val)
        
        if new_f > self.max_freq:
            self.max_freq = new_f

    def pop(self) -> int:
        curr = self.levels_head
        prev = None
        while curr and curr.count < self.max_freq:
            prev = curr
            curr = curr.next
            
        val = curr.items.pop()
        
        if not curr.items:
            self.max_freq -= 1
            
        return val

    def _find_current_freq(self, val):
        count = 0
        curr = self.levels_head
        while curr:
            if val in curr.items:
                count += 1
            curr = curr.next

        return count

    def _get_or_create_level(self, n):
        if not self.levels_head:
            self.levels_head = FrequencyLevel(1)
        
        curr = self.levels_head
        while curr.count < n:
            if not curr.next:
                curr.next = FrequencyLevel(curr.count + 1)
            curr = curr.next

        return curr


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
