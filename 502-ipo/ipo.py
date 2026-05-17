"""
k: number of projects
w: initial capital
n: amount of projects
capital: capital required for ith project
profits: profits for ith project


ok so we need to maximize the capital we can get, maybe a greedy approach or dp would be good to think of.

let's first think of a gredy appproach. If we didn't have the capital restriction we could sort the profits and just start witht he highest
but that's not possible, because of that I also don't see this much as a dp problem

so the issue is that even if we don't have the capital for a project with a lot of profit right now,
we might have in the future after finishing a project

we can first store into a hashmap a touple with the initial indexes:

0: (1, 0)

for example, the first project has a profit and a capital of 1, that way we can alter the order of the arrays  as we want

ok so we search for the capital that gives us the most profit that is inside our budget, select it and pop it, and add to our budget

yeah I think we can do this with a heap, cause

we build the heap in O(n) time, based on the profits, we search for the one that matches our capital while we have k and remove from the heap,
and we do it over and over

I think the overall is something like O(n*k)
"""

import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = list(zip(capital, profits))
        projects.sort()
        heap = []
        j = 0

        for i in range(k):
            while j < n and projects[j][0] <= w:
                heappush(heap, -projects[j][1])
                j += 1
            if not heap:
                break
            w += -heappop(heap)

        return w