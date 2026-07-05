"""
ok provinces are the group of indirectly connected cities, we get a matrix of direct connections

i and j are directly connected, so 

we have no information about indirect connections after more than 1 connection like

a->b->c->d is a indirectly connected to d? I would think so

we have to do a bfs basically for this, we search the neighbors until we run out of it and add

so,we first make the graph i think

graph = {

}

btw is it important that the graph is bidirectional? we will see

so we do bfs if the curent node hasn't been visited already, and add
"""
from collections import defaultdict, deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(set)
        visited = set()
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    graph[i].add(j)
                    graph[j].add(i)
        res = 0
        for orig_node in graph.keys():
            q = deque([orig_node])
            if orig_node not in visited:
                res+=1

            while q:
                node = q.popleft()

                if node not in visited:
                    visited.add(node)
                    neighbors = graph[node]
                    for neighbor in neighbors:
                        q.append(neighbor)

        return res