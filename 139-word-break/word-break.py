"""
word dictionary,
the same word may be used multiple times

can it be separated into words

ok can we model this as a graph?
can we use a hashmap?
can we divide it into multiple subproblems?

it might also look like a sliding window problem

ok I think we can divide into multiple subproblems because if we add anything that isn't in the dict to the current
solution it's just false unless it's in the words and thats O(1)

if a word is contained into another the response is true

why can't we just use sliding window?

because it doesn't seemt o be a place for the window to actually stop rather than finding a word, but then reducing the window would be a lot, let's think about another approach

ok so if i divide it into subproblems... that's it?

l false
leet false
leetcode false

so a recursive approach might work, with memoization I see it, but dp.....

words = [0] * n
for i in s:
    s[:i]
    if the solution to the previous is found, check that the new thing added is in the dictionary, 
    if not set that as false

so for the case of words contained into other words we dont care but for intersections

ok so they shouldnt work so its fine


ok so the problem is that im technically not building on the last subproblem......

so if i dont find a solution can i go back? like for repeated this is tricky

if i use sliding window what

so if we have a solution we check again?

ok so if in dp I store the words up to that point, and then i make some kind of priority...?

ok but the thing is all the string has to be in the dictionary so the problem is with repeated stuff

if i take the longest as priority what
"""
from collections import Counter
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[-1]