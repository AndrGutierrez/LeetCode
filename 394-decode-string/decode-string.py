"""
traverse until finding a closing bracket, pop, multiply, when finding another bracket pop again

if is digit add to queue current digit
if its string add to the current string

if the bracket opens, add digit to the queue


3 2

a c


if the bracket closes we pop from the list the latest...? and add the current
"""
from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:
        multipliers = deque()
        strings = deque()
        curr_multiplier = ""
        curr = ""

        for c in s:
            if c.isdigit():
                curr_multiplier+=c
            elif c == '[':
                if strings != '':
                    strings.append(curr)
                    curr = ''
                multipliers.append(curr_multiplier)
                curr_multiplier = ''
            elif c == ']':
                m = int(multipliers.pop())
                curr = m * curr
                if strings:
                    curr = f'{strings.pop()}{curr}'
            else:
                curr+= c
        return curr