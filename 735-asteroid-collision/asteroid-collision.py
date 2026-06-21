"""
all asteroids move at the same speed

if two asteroids meet, the smaller explodes, if they're the same size, both explode

let's see

we traverse until finding something with a different symbol, then make the comparation and remove from the queue the necessary 

ok so when we find a different symbol, compare with the latest, if the symbol is negative we have to check again with the latest, if its positive we continue

ok so when the s
"""

from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        q = deque()
        n = len(asteroids)
        i = 0
        for asteroid in asteroids:
            if not q:
                q.append(asteroid)
                continue
            if asteroid < 0:
                if q[-1] < 0: 
                    q.append(asteroid)
                    continue
                if -asteroid > q[-1]:
                    while -asteroid >= q[-1]:
                        if -asteroid == q[-1]:
                            q.pop()
                            break
                        if q[-1] <0:
                            q.append(asteroid)
                            break
                        q.pop()
                        if not q: 
                            q.append(asteroid)
                            break
                elif -asteroid == q[-1]:
                    q.pop()
                    continue
            else: q.append(asteroid)
            # latest = q.pop()
            # if (asteroid > 0 and latest < 0) or (asteroid < 0 and latest > 0):
        return list(q)