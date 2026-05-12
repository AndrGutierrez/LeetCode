"""
maximum: some kind of optimization, greedy or dp

ok so the first approach would be some kind of backtracking and recursion, we take a
decision each time of rob vs not to rob, we can optimize later
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Recursive solution
        # res = 0
        # maximums = []
        # def backtrack(curr, optimal, robbed):
        #     if curr >= len(nums)-1:
        #         nonlocal maximums
        #         maximums.append(optimal)
        #         
        #     for i in range(curr, len(nums)):
        #         if i-1 not in robbed and i+1 not in robbed:
        #             robbed.add(i)
        #             backtrack(i+1, optimal+nums[i], robbed)
        #             robbed.remove(i)
        # backtrack(0, 0, set())
        # res = max(maximums)
        # return res
        # Tabulation
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        n = len(nums)
        robbed = [0] * n
        robbed[0], robbed[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            robbed[i] = max(robbed[i-1], robbed[i-2]+nums[i])
        return robbed[-1]