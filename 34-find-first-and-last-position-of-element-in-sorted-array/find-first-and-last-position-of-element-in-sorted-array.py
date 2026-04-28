"""
sorted non decreasing

there's a target

if its sorted then they can be repeated but they cannot be like 878 for example

binary search is the way to go but it stops when finding one, if we traberse when finding it... idk the worst case is all is the same so the time
complexity would be O(n)

so, the best approach is probably to find the first and last appearance, 

there can be cases like this:

[1 8 8 8 9]

where the target is at both sides

i mean we can search at both sides and then we return what we find at one and the other

and for example

[4, 5,7,7,7,8,8,10]

I mean we have to look for another, the latest, in the same half...?

if we take high and low and none is target

4
5
7
7
7
8
8
10

7
8
8
10

8

if we find, we do binary search in the other half recursively
"""
import math
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return (self.binarySearch(nums, target,0))
    
    def binarySearch(self, arr, target, addition):
        if len(arr) == 0: return [-1,-1]

        low = 0
        high = len(arr)-1
        while high >= low:
            mid = low + (high-low)//2

            if arr[mid] == target:

                indexright = self.binarySearch(arr[mid+1:], target, mid+1)
                indexleft = self.binarySearch(arr[:mid], target, 0)
                
                if indexright != [-1, -1]:
                    leftmost = min(indexleft[0], mid) if indexleft[0] >= 0 else mid
                    return [leftmost, indexright[1]+addition]
                elif indexleft != [-1, -1]: 
                    return [indexleft[0], max(mid, indexright[1]) + addition]
                else:
                    return [mid+addition, mid+addition]
            elif arr[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return [-1,-1]