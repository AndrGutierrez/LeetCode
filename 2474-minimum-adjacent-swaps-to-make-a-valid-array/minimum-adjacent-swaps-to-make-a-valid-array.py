"""
minimum adjacent swaps required to make a valid array

valid array:

largest element is last

smallest element is first

this kind of problems remind me of two pointers

ok first of all the most efficient way to get the smallest and largest is with a heap

that we can get both in nlogn time now that we have a heap we could do something with it

there are multiple ways to get this, brute force doesnt seem like a solution

input size suggest O(n) solution, nlogn at most

we might be able to divide this into two subcases,

first:

smallest element is at left of the largest

second:

smallest element is at the right of the largest

in the first case its just the distance to the beggining and the end, in the second
I think it's good enough to move the smallest element to the left and by that,
the largest element is always gonna be 1 step closer to where it should be

so we now have to handle multiple of smallest and largest, in which case the worst
case is lik 1111155555, so we will take the colsest one, worst case is nlogn so i think heap works

so what we will do is heappush with the index, and pick the index which is closest to the edges

"""

from collections import heapq
class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        min_heap = []
        max_heap = []
        n = len(nums)
        if n == 1: return 0
        for i, num in enumerate(nums):
            heappush(min_heap, (num, i))
            heappush(max_heap, (-num, -i))
        mn, mn_index = heappop(min_heap)
        mx, mx_index = heappop(max_heap)
        mx = -mx
        mx_index = -mx_index
        
        if mx_index > mn_index:
            res = (n - 1 - mx_index) + mn_index
        elif mn_index > mx_index:
            res = (mn_index) + (n - mx_index -2)

        else: return 0
        return res 