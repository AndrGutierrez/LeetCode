class Node:
    def __init__(self, val, node = None, prev = None):
        self.val = val
        self.next = node
        self.prev = prev
        self.smallest = None
        self.largest = None

class MinStack:

    def __init__(self):
        self.smallest = None
        self.current = None
        

    def push(self, val: int) -> None:
        if self.current:
            new_node = Node(val, None, self.current)

            new_node.smallest = min(self.current.smallest, val)

            self.current.next = new_node
            self.current = self.current.next
        else:
            self.current = Node(val)
            self.current.smallest = val
            
        
    def pop(self) -> None:
        self.current = self.current.prev
        if self.current: self.current.next = None
        

    def top(self) -> int:
        return self.current.val
        

    def getMin(self) -> int:
        return self.current.smallest
        
"""
val, min, max
-2, -2, -2
0, -2, 0
-1, -2, 0
"""
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()