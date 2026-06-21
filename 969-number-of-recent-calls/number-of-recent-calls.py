"""
delta = t[i] - t[i-1]

we can make an array of sorted t's

return number of requests in the past [t - 3000, t]

we can easily do O(n) if we use a queue and just pop, but not quite popping

so, if we just do a backwards while loop, until the time is > t-3000
"""

class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        i = len(self.requests) - 1
        res = 1
        while i >= 0:
            if t - self.requests[i] > 3000:
                break
            else:
                res+=1
            i-=1
        self.requests.append(t)
        return res


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)