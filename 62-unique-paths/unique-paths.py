"""
m and n <= 100 so we could try backtracking, though we don't need the exact paths but
just the amount.

if we represented the board as a dp 2d array and we get how many possible steps we need to 
reach this, we would be able to do this in mxn time really easy, we just

we assume theres no loops of course.... ok so it is important that we can only move
down or right, that almost confirms this is dp because otherwise this could only be achieved via backtracking. so the amount of ways we can get here is the max between the top and left + 1
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1: return 1
        dp = [[0] * n for _ in range(m)]
        dp[0][1] = 1
        dp[1][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j>=2:
                    dp[i][j] = dp[i][j - 1]
                
                if j == 0 and i >=2:
                    dp[i][j] = dp[i - 1][j]

                if i >=1 and j>=1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]