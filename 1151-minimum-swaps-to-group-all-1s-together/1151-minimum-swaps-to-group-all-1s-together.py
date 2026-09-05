"""
minimum swaps, to place them together in ANY part of the array

we only have the swap operation

minimum sounds like optimization so we could think about dp

the brute force approach would be... calculating all possible swaps and getting the smallest one

that sounds like backtracking that could be optimized as dp

the input size discards 2d dp and it doesnt seem so at first glance

so it could be done with dp if we identified like the groups

maybe longest sequence

ok this is two pointers let's see tomorrow if i can solve it m
"""

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        left = 0
        right = sum(data) 
        n = len(data)
        amount_of_zeros = right - left - sum(data[left:right])
        res = amount_of_zeros
        left+=1
        right
        for i in data[1:(n - right)+1]:
            if data[left - 1] == 0:
                amount_of_zeros -=1 

            if data[right] == 0:
                amount_of_zeros +=1
            res = min(res, amount_of_zeros)
            left+=1
            right+=1



        return res