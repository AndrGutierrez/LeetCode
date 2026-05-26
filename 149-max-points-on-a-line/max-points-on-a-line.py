"""
it asks for a maximum so we could think of greedy or dp, though i dont
see how this can ve into smaller subproblems so lets take dp apart for a sec

its easy to know if dots are in the same line, but to get the maximum number of dots...

we can do a brute force approach since the max is 300, but theres probably other approach

the recursive approach would be something like:

def isInLine():
    for dot in dots:
        getSlopes(dots)

and return the amount of equal slopes? takes O(n^2) and by the input size seems correct
"""
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        slopes = defaultdict(lambda: defaultdict(int))
        visited = set()
        res = 0

        for i in range(n):
            (x1, y1) = points[i] 
            for j in range(n):
                (x2,y2) = points[j]
                
                if j!=i and (x2,y2) not in visited:
                    if x2 != x1:
                        slope = str((y2-y1)/(x2-x1))
                        slopes[i][slope]+=1
                    else:
                        slopes[i][0]+=1
            res = max(res, max(slopes[i].values() or [0]))
        return res+1