"""
ok so its the exclusion 

traverse nums, make a set, traverse nums2, make a set, return the nums that aren't in the set
"""
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [set(), set()]
        nums1set = set(nums1)
        nums2set = set(nums2)
        for num in nums1:
            if num not in nums2set:
                answer[0].add(num)

        for num in nums2:
            if num not in nums1set:
                answer[1].add(num)
        return [list(answer[0]), list(answer[1])]