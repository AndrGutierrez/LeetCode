"""
if left + left+1 + right == 0 add to triplete
else right +=1

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i == 0 or nums[i-1] != num:
                self.twoSum(nums, i, res)
        return res
    
    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[left] + nums[i] + nums[right]
                if s < 0:
                    left +=1
                elif s > 0:
                    right -=1
                else:
                    res.append([nums[i], nums[left] , nums[right]])
                    left +=1
                    right -=1
                    while left < right and nums[left] == nums[left - 1]:
                        left+=1

