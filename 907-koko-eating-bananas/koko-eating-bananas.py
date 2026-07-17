"""
n piles of m bananas

eats k bananas every hour, 

minimum k we need so koko can eat all bananas in h hours

ok so if we were only to find a solution it would be the max number of the array because we would eat all bananas in n hours

so we know the solution is in the range

[1, max(piles)]

so then we can try to check at the middle, between 1, and max(piles) if that's a better solution, 

if it is
we go left

else
we go right

we will do binary search for that, and each one we find will take n time, so it's a time complexity of

O(nlogn)

also we asume k is an integer because if it isnt this is madness

can we make sure we can eat them all with a number if it isnt't traversing it again and again?
"""
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles) 
        low = 1
        high = max(piles)
        res = high
        j = 0
        while high >= low:
            mid = (high + low) //2
            i = 0
            curr = piles[i]
            hours_spent = 0
            for pile in piles:
                hours_spent += math.ceil(pile/mid)

            if hours_spent <= h:
                high = mid - 1
                res = min(res, mid)
            else:
                low = mid + 1
        return res