"""
use two pointers and go from left to right and right to left

if the sum of the left is bigger than the right, add to the right, if they're equal add both

[0,0]
[-1, -1, -1, -1]

ok so there's a right part and a left part and there's something in the middle, empty can count as left and right
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum= sum(nums)
        leftsum = 0
        for i, num in enumerate(nums):
            if leftsum == totalsum - leftsum - num:
                return i
            leftsum+=num
        return -1