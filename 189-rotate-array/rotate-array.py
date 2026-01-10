from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        queue = deque(nums)
        for i in range(k):
            insert = queue[-1]
            queue.appendleft(insert)
            queue.pop()
        
        nums[:] =list(queue)