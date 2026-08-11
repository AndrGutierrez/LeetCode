"""
return MINIMUM number of days for each to get a warmer one... if there's not let it be 0

I think one way could be a heap... but that would be nlogn at best, lets see if theres something better

by the way the obvious is brute force O(n^2)

ok i just researched what a monotonic stack is and it's exactly ts, a decreasing monotonic stack

where if we foind something higher than the last element we pop the last element, we just have to keep track of how much times we pop

well if we also save the index...
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                [index, _] = stack.pop()
                res[index] = i-index
            stack.append((i, temp))
        return res