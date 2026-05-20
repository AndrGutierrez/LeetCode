"""
its the same as the previous one but the obstacle is inf

but it asks the possible unique paths

we could use a bfs approach and search for the paths but that might be too overkill

if theres an obstacle in the end result is 0
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-float("inf")] *n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] !=1:
                    # if i ==0 and dp[i-1][j] > -float("inf"):
                    #     dp[i][j] = 1
                    # if j ==0 and dp[i][j-1] > -float("inf"):
                    #     dp[i][j] = 1
                    if i == 0 and dp[i][j-1]== -float("inf") and j > 0:
                        dp[i][j] =  -float("inf")
                        continue
                    if j ==0 and dp[i-1][j] == -float("inf") and i>0:
                        dp[i][j] =  -float("inf")
                        continue
                    if i == 0 or j ==0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = max(dp[i-1][j], 0) + max(dp[i][j-1], 0)
                        if dp[i][j] == 0: dp[i][j] = -float("inf")
        res = dp[-1][-1] if dp[-1][-1] != -float("inf") else 0

        print(dp)
        return res