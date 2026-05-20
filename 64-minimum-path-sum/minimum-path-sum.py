"""
maximize the sum of all numbers along a path from top left to bottom right

only can move down or right

ok so first approach is just to find all possible ways to have a path but its probably
some kind of O(n^3) and grid can be up to 200x200

its a minimization problem so we can think of greedy, dp, etc

if its dp can we divide this into smaller subproblems?

for example the solution for a smaller grid at certain point can be included into the
solution of a bigger grid?

important to note, all numbers are positive
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[float("inf") for _ in range(n)] for i in range(m)]
        dp[0][0] = grid[0][0] 
        for i in range(m):
            for j in range(n):
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                    print()
                if j == 0 and i > 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                elif i>0 and j>0:
                    dp[i][j] = min(dp[i-1][j] +  grid[i][j], dp[i][j-1] + grid[i][j])

                    
        print(dp)

        return dp[-1][-1]