"""
fewest number of coins, if it cannot be solved return -1

so its an optimization problem, 

it can be greedy, dp, idk

we can have at most 12 coins, so it might be worth it to look at a recursive solution

so, we make a tree, and we can take a decision of either taking the coin or not, and then the solution would be the shortest branch with a 
dfs or smth that sums up to that

but we do need only those branches, the other ones are worthless

can this be divided into smaller subproblems?

like if we add to the amount or coins we have to recalculate everything but...
for example

14
[3, 5]

if we take the most greedy approach we go

5
5
3

wops

5, 3, 3, 3

well the amount of coins is small enough to just try

if i take lets say

in that case
1: -1
2: -1
3: 1 ([3])
4: -1
5: 1 ([5])
6: 2 ([3,3])
7: -1
8: 2 ([5,3])
9: 3 ([3,3,3])
10: 


ok what's our subproblem

our subproblem is all the i < amount

ok so we try with all coins we have, and we use the least needed, we always start at 1,

so we try with all coins with the least needed, we eventually get to a base case

then we go to the next one, 
"""
import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        # coins = sorted(coins)
        for i in range(1, amount+1):
            remaining = i
            for coin in coins:
                remaining = i-coin
                if remaining >= 0:
                    dp[i] = min(dp[i], dp[remaining]+1)
        # so time complexity os O(nk) no n² as i thought
        res = -1 if dp[-1] == math.inf else dp[-1]
        return res