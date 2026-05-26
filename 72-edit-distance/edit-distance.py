"""
minimum number of operations required to convert

lowercases in english only

ok so this is very likely an optimization problem, maybe dp or greedy algorithms

if it's dp we should be able to build the overall solution with smaller subcases

but we probably should consider the brute force solution first, by the word lenght it could be a backtracking problem

but the recursive solution is trying all possible operations in every character all  possible combinations, so that's a
lot and maybe even hard to code

ok so first we take the length, 

if word1 < word2:
    we need the length diff + the diff of the most similar inside
if the length is equal:
    we need the diff 
if word2 > word1:
    we need the diff + the diff of each one like its just the equal length case

ok so how do we know the most similar diff when deleting that looks like the most important problem

we can evaluate on each iteration but that's probably not very efficient, can we use dp to build up the solution?

but if we replace first it seems like we can get a better solution, how do we know what to replace

we can get different variations of the word1, see which one is closer, and then build on top of that, like trying with each operation,
decide and store 
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        if l1 == 0:
            return l2
        if l2 == 0:
            return l1

        dp = [[0] * (l2 +1) for _ in range(l1 + 1)]

        for i in range(1, l1+1):
            dp[i][0] =  i
        for i in range(1, l2 +1):
            dp[0][i] = i
        
        for i in range(1, l1 + 1):
            for j in range(1, l2 +1):
                if word2[j-1] == word1[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = (
                        min(
                            dp[i-1][j],
                            dp[i][j-1],
                            dp[i-1][j-1]
                        ) + 1
                    )
        return dp[l1][l2]