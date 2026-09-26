"""
time needed to complete ith job

time the jth worker can work each day

1 job per worker, so each worker completes exactly one job

minimum number of days to complete all jobs

so we have to distribute the job in an optimal way

doesn't seem dp

can i solve this with a graph?

first let's see, the absolute minimum is:

math.ceil(max(jobs)/max(workers))

maximum is

math.ceil(max(jobs)/min(workers))

solution is somewhere in the  because there might be cases like

[10, 10]
[1, 10]

even though one can complete in one day the other one is a bottleneck

[13, 50, 50]
[13, 5, 25]

I'm trying to see if there's a case where the optimal solution does not include math.ceil(max(jobs)/max(workers))

because if it is we can take that as a base and then start adding up

well for example the one in the problem... either way takes two days....
"""
import math
class Solution:
    def minimumTime(self, jobs: list[int], workers: list[int]) -> int:
        jobs = sorted(jobs)
        workers = sorted(workers)
        minimum = -float('inf')
        for job, worker in zip(jobs, workers):
            minimum = max(minimum, math.ceil(job/worker))
        return minimum