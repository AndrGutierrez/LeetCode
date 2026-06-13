"""
maximum AVERAGE CONTIGUOUS subarray

ok so first numbers can be negative

ok so this sounds like sliding window

but also like dp

but the size of the window is constant i think this is pretty traightforward

ok so thats O(nk), can we optiimze it?????

if we get a O(nlogn)...................................................

well we can just instead of suming on each iteration add and substract
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        res = sum(nums[0:k])
        latest = res
        # if n == 1: return nums[0]
        for i in range(n-k):
            left = i
            right = i + k
            latest = latest + nums[right] - nums[left]
            res = max(res, latest)
        return res/k