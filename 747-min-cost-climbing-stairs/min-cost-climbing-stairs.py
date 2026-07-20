"""
ok an optimization problem, it might be dp

ok so if it is a dp problem we can divide it into smaller subproblems, can we?

seems like, we get the cheapest way to climb each time

we can make an array to get the cheapest way to get to each i, since we can go jump twice the cheapest
way we can get here will always be the minimum between

dp[i-2] + cost[i-2] and dp[i-1] and cost[i-1]
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0, 0]
        for i in range(2, len(cost)+1):
            dp.append(min(dp[i-2] + cost[i-2], dp[i-1]+ cost[i-1]))
        return dp[len(cost)]