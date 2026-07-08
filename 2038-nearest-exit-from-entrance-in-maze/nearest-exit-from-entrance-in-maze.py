"""
only horizontal and vertical movement

cannot go outside the maze or cross walls

find nearest exit

we could use backtracking but that would help us find some, and then we would find the shortest

an exit is a cell that is in an edge 

so we just have to make a graph connecting this and find the nearest exit through bfs seems simple enough
"""
from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        res = 0
        graph = defaultdict(list)
        visited = set()
        visited.add(f'{entrance[0]},{entrance[1]}')
        for i in range(m):
            for j in range(n):
                if i >= 1:
                    if maze[i-1][j] == '.':
                        graph[f"{i},{j}"].append(f"{i-1},{j}")
                if j >= 1:
                    if maze[i][j-1] == '.':
                        graph[f"{i},{j}"].append(f"{i},{j-1}")
                if i < m - 1:
                    if maze[i+1][j] == '.':
                        graph[f"{i},{j}"].append(f"{i + 1},{j}")
                if j < n - 1:
                    if maze[i][j+1] == '.':
                        graph[f"{i},{j}"].append(f"{i},{j+1}")

        # print(graph['3,2'])

        q = deque([f'{entrance[0]},{entrance[1]}'])
        exit_found  = False

        while q:
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
                        [i, j] = [int(coord) for coord in neighbor.split(',')]
                        is_exit = i == m - 1 or j == n - 1 or i == 0 or j == 0
                        if (is_exit) and (i != entrance[0] or j != entrance[1]): 
                            exit_found = True
            res +=1 
            if exit_found: break

        if exit_found: return res
        else: return -1