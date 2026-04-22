"""
this is DP or greedy

[7, 8, 6]
"""
import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = -math.inf

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum+=num
            max_sum = max(curr_sum, max_sum)

        return max_sum