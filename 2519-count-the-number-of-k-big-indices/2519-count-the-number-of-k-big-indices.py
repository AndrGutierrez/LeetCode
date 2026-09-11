import heapq
class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        n = len(nums)

        meets_first_criteria = [False] * n
        heap = []
        res = 0
        for i, num in enumerate(nums):
            # there's k indices such that idx1 < i
            if i >= k:
                # from these, there's k indices idx1 such that nums[idx1] < nums[i]
                # the importance of the heap in here is that we don't need to calculate on each
                # iteration and we are able to keep the indices
                meets_first_criteria[i] = -heap[0] < num 
            heapq.heappush(heap, -num)
            if len(heap) > k: heapq.heappop(heap)
        heap = []

        for i, num in reversed(list(enumerate(nums))):
            if n-i-1 >=k:
                res+= meets_first_criteria[i] and -heap[0] < num                
            heapq.heappush(heap, -num)
            if len(heap) > k: heapq.heappop(heap)

        return res