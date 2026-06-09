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
        left = 0
        right = 1
        i = 0 
        n = len(nums)
        while right < n:
            if nums[left] != 0:
                left+=1
                right = left +1
            elif nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left = left+1
                right = left + 1
            else:
                right +=1
            i+=1
            #if i >= 100:
            #    print("a")
            #    break