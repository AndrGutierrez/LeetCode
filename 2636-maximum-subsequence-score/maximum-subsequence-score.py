"""
both arrays have same length

important, all numbers are positive

we can get a heap with the indexes,

we can make two heaps maybe, 

there might be cases like

1     2   3  4  5  6
[10, 11, 12, 1, 1, 1]
[100,   100,  100, 1, 1, 99]

so the maximum would be index

2, 3, 6
"""
import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        heap = []
        pairs = [(a, b) for a, b in zip(nums1, nums2)]
        pairs.sort(key= lambda x: -x[1])

        top_k_heap = [x[0] for x in pairs[:k]]
        heapq.heapify(top_k_heap)

        top_k_sum = sum(top_k_heap)

        # maximize nums2
        res = top_k_sum * pairs[k-1][1]
        # maximize nums1,  
        for i in range(k, len(nums1)):
            top_k_sum -= heapq.heappop(top_k_heap)
            top_k_sum += pairs[i][0]
            heapq.heappush(top_k_heap, pairs[i][0])
            
            # here we check if this is better,
            # because we might change the (num2, nums1) which we maximized originally
            # by getting the gratest nums2, but this way we get combinations that might be better
            res = max(res, top_k_sum * pairs[i][1])
        return res