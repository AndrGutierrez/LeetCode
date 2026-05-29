from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
        q = deque()
        curr = ""
        for c in s:
            if c.isalnum():
                curr+=c
            else:
                if curr is not '':
                    q.appendleft(curr)
                curr = ''            
        if curr is not '':
            q.appendleft(curr)
        return " ".join(list(q))