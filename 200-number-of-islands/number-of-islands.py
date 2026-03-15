""" Islands
make each one a node, each node has north, south, east, and west,

save an array of visited nodes, 

I would have to use bfs but we might go in circles...

max is 9000

so we can assume this can take long

ok, so save each one, keep a queue of already visited nodes

count = 0
traverse the matrix until find one, do bfs, when finished, add 1 to count keep traversing, until finished,then return count
"""

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.res = 0
        graph = {}
        self.visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                name = f"{i},{j}"
                nodes = []
                if i > 0:
                    if grid[i-1][j] == '1': nodes.append(f"{i-1},{j}")
                if i < len(grid) - 1:
                    if grid[i+1][j] == '1': nodes.append(f"{i+1},{j}")

                if j > 0:
                    if grid[i][j-1] == '1': nodes.append(f"{i},{j-1}")

                if j < len(grid[i]) - 1:
                    if grid[i][j+1] == '1': nodes.append(f"{i},{j+1}")

                graph[name] = nodes
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    node = f"{i},{j}"
                    if node not in self.visited:
                        self.bfs(node, graph)      
        return self.res
        
    def bfs(self, initial, graph):
        q = deque([initial])
        self.visited.add(initial)
        while q:
            current = q.popleft()
            for neighbor in graph[current]:
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    q.append(neighbor)
        self.res+=1