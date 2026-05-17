"""
this is a dp problem, so we can solve it by dividing it into its smaller subproblems,

whichwould be all the subarrays from left to right

so for these

10

10 9

10 9 2

10 9 2 5

etc

we can do it with dp, we get to a number and then we search for the immediate smaller than what we had,

this os O(nxsomething) but why isnt O(n²)? well the worst case i think is getting to the end and finding its nearest smallest is the first element but that an array thats decreasing in its first half and then increasing in its second

I think that's O(n² but ok)
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums))
        n = len(nums)
        res = 1
        for i in range(n):
            maxLatest= max([dp[j] for j in range(0,i) if nums[j] < nums[i]] +[-float("inf")])
            if maxLatest != -float("inf"):
                # print(i, maxLatest)
                dp[i] = maxLatest + 1
                res = max(res,dp[i])
            else:
                dp[i] = 1
        return res