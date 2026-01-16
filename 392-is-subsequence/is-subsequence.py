from collections import deque
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        arr =list(s)
        full_text = list(t)

        q = deque(arr)
        for char in full_text:
            if not q: return True
            if q[0]  == char:
                q.popleft()

        if q: return False
        else: return True