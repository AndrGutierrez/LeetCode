"""
maximum consecutive 1's but we can flip at most k

ok so we can make a sliding window, that keeps going as long as we have k, if we run out of k, finish the window, 

in the end add k if remaining

ok so we add to the window, if we still have k, if we dont we reduce and restore k if the last one was flipped
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        left = 0
        right = 0
        while right < n:
            if nums[right] == 1: 
                right+=1

            elif k >=1:
                k-=1
                right +=1

            else:
                if nums[left] == 0: k+=1
                left+=1
            
            res = max(res, right-left)

        return res