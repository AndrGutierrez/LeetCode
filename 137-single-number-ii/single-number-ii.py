from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for num in nums:
            if counts[num] == 1: return num