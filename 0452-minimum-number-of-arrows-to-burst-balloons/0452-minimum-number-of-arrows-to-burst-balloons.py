"""
minimum amout of balloons needed

so this is an interval problem we maybe want to sort the intervals first, then we would have like

[1, 6], [2, 8], [7, 12], [10,16]

if the intervals overlap we need an arrow, then we would need the amount of balloons - overlapping intervals?

ok so the problem is if several overlap how did we that? i think it was kind of a k 

we got coordinates x1, x2, if x1 > k it doesnt overlap and else we set k to x2

well its not - the amount of overlapping intervals but the amount of ...

this might be greedy?

ok so we set like an end, to the first, if the next start before the current end they overlap and we -=1, if not we set the new k
"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x: x[0])
        k = -float('inf')
        overlapping = 0

        for x1, x2 in points:
            if x1 <= k:
                overlapping += 1
                k = min(k, x2)
            else:
                k = x2

        return len(points) - overlapping