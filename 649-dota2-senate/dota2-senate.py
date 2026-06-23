"""
multiple rounds

operations: 

- ban rights of other senator
- announce victory if all remaining are from the same party

R =  Radiant party
D = Dire party

each senator plays with the best strategy, that is...?

while there isnt a victor:
    if are all remaining from the same party:
        return party
    else:
        ban next of the opposite party (we could remove it from the array)

we can make an amount of bans and make a queue for the next round

if there's still a queue of another we continue, if there'sn't return
"""
from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        direq = deque()
        radiantq = deque()
        n = len(senate)
        for i in range(n):
            senator = senate[i]
            if senator == "R":
                radiantq.append(i)
            else: direq.append(i)
        
        while radiantq and direq:
            turnr = radiantq.popleft()
            turnd = direq.popleft()

            if turnd < turnr:
                direq.append(turnd + n)
            else:
                radiantq.append(turnr + n) 

        if radiantq:
            return "Radiant"
        else: 
            return "Dire"