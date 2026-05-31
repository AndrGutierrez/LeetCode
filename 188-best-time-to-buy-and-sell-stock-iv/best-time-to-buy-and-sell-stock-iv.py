"""
ok so this is an extension of buy and sell stock III, so it's pretty straightforward, just a generalization of the 
other approach... no, well yes the input size is fairly small so it's safe to say a O(kn) time complexity is allowed,
"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0: return 0
        costs = [float("inf")] * (k+1)
        profits = [0] * (k + 1)

        n = len(prices)
        for price in prices:
            for j in range(k ):
                costs[j + 1] = min(costs[j + 1], price - profits[j])
                profits[j + 1] = max(profits[j + 1], price - costs[j + 1])
        return profits[k]