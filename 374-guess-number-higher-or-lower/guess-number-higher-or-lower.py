# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

"""
ok so this is binary search then

ok so when we call guess we get if it's grater or smaller than our target

obviously brute force O(n) is the easiest but this screams binary search

so we need to set a pointer
"""
class Solution:
    def guessNumber(self, n: int) -> int:
        # return -1
        if n == 1: return 1
        low = 0
        high = n
        while True:
            mid = (low + high) //2
            # higher than target
            if guess(mid) == -1:
                high = mid -1
            # lower
            if guess(mid) == 1:
                low = mid + 1
            #solved
            if guess(mid) == 0:
                break
        return mid