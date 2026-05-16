"""
median of the two sorted array
if the median is shared between two elements, return the average of those elements


O(log(m+n))

so the O(nlogn) solution would be just merge the arrays, sort again and return the element in the middle

that's not possible though, it must be O(log(m+n))

the most common O(log(n)) thing is often binary search or other kind of graph based algorithm

we can merge the arrays, and then search for the element in beween, though this doesn't ever state the numbers are unique

well we can just merge the array and search for the number in between the two middle stuff

no there might be muiltiple elements in between... well we might be onto something...

lets say 

[1 3 99 100] 
[2 5 10]

[1 2 3 5 10 99 100]

if we take it as

[1 3 99 100 2 5 10]

if we take the median of both.......

[12345]
[6789]

           
"""

import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        total = m + n
        maxHalfSize = (total + 1) // 2

        low = 0
        high = m

        while True:
            take1 = low + (high-low)//2
            take2 =  maxHalfSize - take1

            maxleft1= -math.inf if take1 == 0 else nums1[take1-1]
            minright1 = math.inf if take1 == m else nums1[take1]
            
            maxleft2 = -math.inf if take2 == 0 else nums2[take2 - 1]
            minright2 = math.inf if take2 == n else nums2[take2]

            if maxleft1 > minright2:
                high =  take1 -1
                continue

            if maxleft2 > minright1:
                low = take1 +1
                continue 
            
            median = max(maxleft1, maxleft2)
            if total % 2 == 1:
                return median
            else:
                return (median + min(minright1, minright2))/2