"""
ok so it's just giving the kids candies and check if it's bigger than all the other max?
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxnum = max(candies)
        res = [0]*len(candies)
        for i in range(len(candies)):
            res[i] = extraCandies+candies[i] >=maxnum
        return res