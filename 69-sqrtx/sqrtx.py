import math
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        
        low = 2
        high = x//2

        while  low <=high:
            mid = low +(high-low) //2
            num = mid*mid
            if num >x:
                high = mid -1
            elif num<x:
                low = mid +1
            else: return mid
        return high