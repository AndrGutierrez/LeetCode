"""longest palindrome

ok so this is very general, first of all the brute force:

we can get all the possible substrings, and check which one is a palindrome, and select the longest, but I think that's something like O(n³)

can we divide this into smaller subproblems?

the smaller subproblems would be the longest palindrome for each substring

even a palindrome can be part of another palindrome
"""
import math
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0]*n for i in s ]
        start=0
        end=0
        for i in range(n, -1, -1):
            for j in range(i+1, n, 1):
                # this part can be understood looking at the table of the explanation video
                dp[i][j] = s[i] == s[j] and ((j-i) <=2 or dp[i+1][j-1])
                # the and is basically if the found palindrome is bigger
                if dp[i][j] and j-i > end - start:
                    start = i
                    end =j
        
        return s[start:end+1]