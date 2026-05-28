"""
maximization, whats the maximum we can get with two transactions at most

ok so asume we can just buy one stock a day

since its maximization we can think of greedy or dp

lets first think about brute force which is kind of backtracking

we evaluate every possible action, buy or not buy, sell or not sell every day, 
I think thats kind of 2^n because every time the options grow double lol

ok so lets think about dp, so whats the smaller subproblem....
for each day, decide, then on top of that evaluate if adding a new day we can make more profit
 gonna make a table in my notebook
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t1_cost, t2_cost = float("inf"), float("inf")
        t1_profit, t2_profit = 0, 0

        for price in prices:
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)

            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price -  t2_cost)

        return t2_profit