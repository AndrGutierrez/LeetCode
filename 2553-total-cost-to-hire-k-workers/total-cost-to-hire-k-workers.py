"""
n workers, k sessions, one worker each session

candidates is just an arbitrary number of how will we pick(?

workers can only be chosen once

return cost to hire k workers

ok so we gotta get the cheapest workers in the range of "candidates" but after
we hire someone that range changes

we also break ties by chosing the smaller index

if we make a heap each time we remove it is O(n) and that klogk times, though deleting from the array k times..... but we can swap delete i think 

and if 2(candidates)< len(costs) just pop the lowest cost

ok so maybe instead of deleting from the array which might be more complex we can add to the heap, if we removed an element from the right it would be the next to thing and
if element from right, the one in the left
"""
import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        res = 0

        if 2*candidates >=n:
            heapq.heapify(costs)
            for i in range(k):
                res+=heapq.heappop(costs)
            return res
        left = [(costs[i], i) for i in range(candidates)]
        right = [(costs[n-candidates+i], (n-candidates+i)) for i in range(candidates)]
        selected_candidates = left + right
        left_ref = candidates
        right_ref = n - candidates
        heapq.heapify(selected_candidates)

        for i in range(k):
            cost, index = heapq.heappop(selected_candidates)
            res+=cost
            if left_ref >= right_ref:
                continue
            if index < left_ref:
                heapq.heappush(selected_candidates, (costs[left_ref], left_ref))
                left_ref +=1

            if index >= right_ref:
                right_ref -=1

                heapq.heappush(selected_candidates, (costs[right_ref], right_ref))

        return res
            #selected = heapq.heappop()