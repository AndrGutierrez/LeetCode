from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        start = len(digits) - 1
        q = deque()
        carry = 1
        for i in range(start,-1, -1):
            if digits[i]+carry >=10:
                q.appendleft(int(str(digits[i]+1)[-1]))
                carry = 1
            else:
                q.appendleft(digits[i]+carry)
                carry = 0
        if carry == 1: q.appendleft(1)
        return list(q)