"""
delta = t[i] - t[i-1]

we can make an array of sorted t's

return number of requests in the past [t - 3000, t]

we can easily do O(n) if we use a queue and just pop, but not quite popping

so, if we just do a backwards while loop, until the time is > t-3000

we can do the while loop once, if the diff between the first and the current is > 3000,

popleft
"""

class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[-1] - self.requests[0] > 3000:
            self.requests.popleft()
        return len(self.requests)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)