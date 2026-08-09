"""
return minimum number of intervals (some kind of optimization(?))

minimum number of intervals to remove for make the rest non overlapping

so in example 1 we remove 1 interval, the rest are non overlapping, (it seems "overlapping" is non inclusive)

i think we could do kind of a brute force in O(n^2) but for the input size this has to be at least O(nlogn), most likely O(n)

i think if we sort it would be easier but there's gotta be something better
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        n = len(intervals)
        res = 0
        k = -float('inf')
        for x, y in intervals:
            if x >= k:
                k = y
            else:
                res+=1
        return res