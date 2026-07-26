"""
at first this sounds like sliding window... or queue

though those problems are often O(n) and the input size suggests O(n^2) so it could
be a 2d dp problem

so it is a dp problem if we can divide the problem into smaller subproblems, 
what's our base subproblem, the substrings of text1?

ok so it's essentially the smallest one they share

its important to note its the amount of subsequences and not get all possible subsequences

also I discarded brute force because of the input size, brute force is absolutely more than O(n^2), well we would need to backtrack all possible combinations of text1 in their order like

lets draw the graph
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text2[i] == text1[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]