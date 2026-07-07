"""
there's only one way to travel between cities

it's a directed graph, there are cities that cannot go to city 0

we have to get the minimum amount of connections we have to change in order to go to city 0

ok so we make the graph based on the array, then... i mean the easiest way to think of this is as a linked list but...

like the thing is we just need to flip the backwards connections because there's only one way, so if we can't, we
just flip and try again were we tried, we probably also need a list of visited nodes

ok so you miscalculated, if the current path cannot get to 0, and the node hastn been visited we have
"""
from collections import deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj_list = defaultdict(set)
        for origin, target in connections:
            adj_list[origin].add((target, True))
            adj_list[target].add((origin, False))

        q = deque([0])
        visited = set([0])
        res = 0
        while q:
            node = q.popleft()
            for val, in_connections in adj_list[node]:
                if val not in visited:
                    res += in_connections
                    q.append(val)
                    visited.add(val)

        return res