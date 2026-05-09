"""
get all possible ways to climb and n is fairly small so it might be a recursion problem

its 1 or two steps

I think this can be backtracking because we try all the possible decissions, we make
a tree where we have the possibility to chose one or two

ok but if we take this as the knapsack problem, we can have a table...?

i can save how many do i need for n-1 and calculate adding 1?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        solutions = [0] * (n+1)
        solutions[1]= 1
        solutions[2]= 2
        for i in range(3, n+1):
            solutions[i] = solutions[i-1] + solutions[i-2]
        return solutions[n]