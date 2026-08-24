
"""
partition into unique substrings

when I hear substring I can think of sliding window or queues, but let's see

however the problem asks for the number of possible solutions, but no the solution themselves, that might be DP.

the input size discards any backtracking approach, though that might be a reson for this to be dp

and we're asked for a minimum, that sounds like optimization, this could be dp, again by the input size it should be 1D dp (though there are
other multiple array 2d approaches but i dont think thats the case)

only english lowercase letters

sliding windows seems fine though, is there any case where this wouldn't work?

we would make like a hashmap of the current window, and check if the thing is not in the current window

so the algorithm is the following:

initialize hashmap
traverse the string, if the next char is not in the map, continue, if it is restart the map and set the left pointer to the current, and add 1 to the solution
"""
class Solution:
    def partitionString(self, s: str) -> int:
        res = 0
        seen = {}
        i = 0
        while i < len(s):
            c = s[i]
            if c in seen:
                seen = {}
                res+=1
                continue
            else: 
                seen[c] = 1
                if i == len(s)-1: res+=1
            i+=1
        return res