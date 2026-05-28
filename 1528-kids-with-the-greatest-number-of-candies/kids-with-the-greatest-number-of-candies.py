"""
by the size of the input it seems this is brute force, but is there a more efficient approach than just adding and checking if the current
is bigger than all the others?...

let's try brute forcing and if it passes it passes, not very long to implement and the input sizes suggests thats the solution,
also this is an easy problem
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        total_candies = [0] * n  
        maximum = max(candies)
        for i in range(n):
            total_candies[i] = (candies[i] + extraCandies) >= maximum
        


        return total_candies
