"""
all factors of n sorted

return kth factor of n

given the input size this can be solved in O(n) yes I think it's very easy, we just brute force?

we do for i in range n, until we get to k? 

lets do it the implementation is simple so we won't lose much time if this doesnt work
"""
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, n + 1):
            if n % i == 0:
                k-=1
            if k == 0: return i
        return -1
