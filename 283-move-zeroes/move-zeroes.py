"""
move zeros to last in place

ok so maybe we can use two pointers

we keep the left at the 0 and the right to the element we find, thats different from 0, then swap until we get to the end

[0, 1, 2, 0, 3]
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 #writer pointer
        right = 0 #reader pointer
        n = len(nums)
        while right < n:
            if nums[right] != 0:
                nums[left] = nums[right]
                left+=1
            right +=1
            
        for i in range(left, right):
            nums[i] = 0
