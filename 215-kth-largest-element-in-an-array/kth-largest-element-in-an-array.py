"""
return the kth largest element of the array
so it seems we cannot sort and then check because otherwise we would lose it

i know this is a heap problem so if I look it as a heap

I can heapify the array, then.............

i can heapop k times?
"""
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for n in nums:
            heapq.heappush(max_heap, -n)
        for i in range(k):
            res = -heapq.heappop(max_heap)
        return res