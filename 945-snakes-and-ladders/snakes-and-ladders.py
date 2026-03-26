"""
important: next must be in the range
[curr +1, min(curr+6, n²)] (so basically max steps i can give launching the dice once)

we must take the snakes an d ladders

so what about not making a connection with neighbors if  has a ladder...

ok so make the relations to the neighbor at the right (except for the ones at the top) if it has a snake or a ladder just change the connection,

seems like if we finish a snake or a ladder we cannot advance without rolling again

so we count the steps til we move 6 (maybe using node values for that) or we found a snake or a ladder

ok but if it's shorter to not land on a snake or a ladder we just do the thing

fairly small amount of squares so we can test by brute force

have to build graph
"""
import copy
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [None] * (n**2 + 1)
        label = 1
        columns = list(range(0, n))
        for row in range(n-1, -1, -1):
            for column in columns:
                cells[label] = (row, column)
                label +=1
            columns.reverse()
        distance = [-1] * (n*n+1)
        q = deque([1])

        distance[1] = 0
        while q:
            curr = q.popleft()
            for next in range(curr + 1, min(curr+6, n**2) + 1):
                row, column = cells[next]
                destination = (board[row][column] if board[row][column] != -1 else next)
                if distance[destination] == -1:
                    distance[destination] = distance[curr]+1
                    q.append(destination)

        return distance[n*n]