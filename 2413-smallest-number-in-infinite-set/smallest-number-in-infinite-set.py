"""
ok so if for example you pop 1, 2, 3, 4 5,

so each time we "pop" we can just add 1, 

 but what if you want to add 2 and 4 back and pop again

i think we can use a heap for the "added back" and that's finite
"""

import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.set = set()
        self.curr = 0
    def popSmallest(self) -> int:
        if not self.heap:
            self.curr+=1 
            return self.curr
        num = heapq.heappop(self.heap)
        self.set.discard(num)
        return num
    def addBack(self, num: int) -> None:

        if num not in self.set and num <= self.curr:
            heapq.heappush(self.heap, num)
            self.set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)