"""
enter or exit once, in one second

non decreasing array (sorted) which represents arrival time

0: wants to enter
1: wants to exit

person with smallest index goes first (priority queue?)

return arraw of the time the person crosses the door


I mean since it's sorted I think we don't have to use a heap, we just need a queue?

traverse both arrays and make tuples such as

person: (index, time, state)

so we traverse the queue, we save latest status.

yes we can have two queues:

entering: []
exiting: []

with the indexes

and depending on the latest, we just chose which queue to pop from, and since this is sorted its fine

ok I forgot to consider arrival time, so we will do a while loop, we will do it while
we have people entering and exiting
"""

from collections import deque
class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        n = len(arrival)
        entering = deque()
        exiting = deque()
        res = [0]*n
        for i in range(n):
            if state[i] == 0: entering.append((i, arrival[i]))
            elif state[i] == 1: exiting.append((i, arrival[i]))

        second = 0
        latest_use = None
        curr_entering = deque()
        curr_exiting = deque()
        while True:
            while entering and entering[0][1] == second:
                curr_entering.append(entering.popleft())
            while exiting and exiting[0][1] == second:
                curr_exiting.append(exiting.popleft())

            if latest_use == None or latest_use == 'exit':
                latest_use = None
                if curr_exiting:
                    res[curr_exiting.popleft()[0]] = second
                    latest_use = 'exit'
                elif curr_entering:
                    res[curr_entering.popleft()[0]] = second
                    latest_use = 'enter'

            elif latest_use == 'enter':    
                latest_use = None
                if curr_entering:
                    res[curr_entering.popleft()[0]] = second
                    latest_use = 'enter'
                elif curr_exiting:
                    res[curr_exiting.popleft()[0]] = second
                    latest_use = 'exit'          
            
            second+=1

            if not (curr_entering or curr_exiting or exiting or entering): 
                break

        return res