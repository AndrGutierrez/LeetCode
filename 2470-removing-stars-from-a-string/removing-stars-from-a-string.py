"""
operations: 

chose star
remove non star at the left and star

return string after that

ok so we can make a queue and each time we find a star we pop and then return string
"""

from collections import deque
class Solution:
    def removeStars(self, s: str) -> str:
        q = deque()
        for c in s:
            if c == "*":
                q.pop()
            else:
                q.append(c)
        
        return "".join(list(q))