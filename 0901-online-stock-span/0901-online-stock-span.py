"""
maximum number of consecutive days when the stock was less or equal than ith day, going backwards

ok but it's the maximum right after, like for example

[97, 98, 100, 99]

the response is

[1, 2, 3, 1]

even though theres a sequence smaller than 99 it doesnt matter because its not right after it

the obvious solution is brute force wich is most likely O(n^2) evaluating each case individually but i think we can use a monotonic stack 
(we could at leats use a heap)

ok no because we dont get the array straightaway

ok but we can keep a 

"""
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append((price, res))
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)