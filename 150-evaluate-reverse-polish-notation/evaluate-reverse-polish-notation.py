from collections import deque
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        q = deque()
        for token in tokens:
            match token:
                case '*':
                    current = int(q.pop())
                    last = int(q.pop())
                    q.append(current*last)
                case '+':
                    current = int(q.pop())
                    last = int(q.pop())
                    q.append(current+last)

                case '-':
                    current = int(q.pop())
                    last = int(q.pop())
                    q.append(last-current)

                case '/':
                    current = int(q.pop())
                    last = int(q.pop())
                    q.append(int(last/current))

                case _:
                    q.append(token)
        return q.pop()