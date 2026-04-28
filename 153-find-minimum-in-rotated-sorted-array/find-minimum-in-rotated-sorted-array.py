"""
ok its sorted but rotated at some point i solved something like this already

return minimum element of array

here we dont need to know if its rotated because it's assumed to be rotated i guess, but it can be 

ok sorted so probably binary search or smth

if i find the index where its rotated i can do two searches and thats it

if the final number is smaller than middle go right else go left and i think thats pretty much the result
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0] or len(nums)==1: return nums[0]
        high = len(nums) - 1
        low = 0
        while high >=low:
            mid = low+(high-low)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] > nums[-1]:
                low = mid+1
            elif nums[mid] < nums[-1]:
                high = mid -1
