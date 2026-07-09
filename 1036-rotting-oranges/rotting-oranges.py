"""
ok this seems pretty straightforward, bfs, each "level" is a minute

we create the graph based on the array, 

there's a the case if there's two rotten oranges in the beggining  

so what we actually have to do is visit all the neighbors of rotten oranges if they havent been visited, update
and repeat
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        graph = defaultdict(list)
        m = len(grid)
        n = len(grid[0])
        orange_amount = 0
        initial_rotten_amount = 0
        initial_fresh_amount = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 or grid[i][j] ==2:
                    orange_amount+=1
                    if grid[i][j] == 2:
                        initial_rotten_amount += 1
                    if grid[i][j] == 1:
                        initial_fresh_amount += 1

                if i >=1:
                    if grid[i - 1][j] == 1 or grid[i - 1][j] == 2:
                        graph[(i, j)].append((i - 1, j))
                if j >=1:
                    if grid[i][j - 1] == 1 or grid[i][j - 1] == 2:
                        graph[(i, j)].append((i, j - 1))
                if i < m - 1:
                    if grid[i + 1][j] == 1 or grid[i + 1][j] == 2:
                        graph[(i, j)].append((i + 1, j))
                if j < n - 1:
                    if grid[i][j + 1] == 1 or grid[i][j + 1] == 2:
                        graph[(i, j)].append((i, j + 1))
        if orange_amount == 0 or initial_fresh_amount == 0: return 0
        if  initial_rotten_amount == 0: return -1
        visited = set()
        res = 0

        while True:
            new = 0
            update = []
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        if (i, j) not in visited:
                            new+=1
                            visited.add((i, j))
                            neighbors = graph[(i, j)]
                            for node in neighbors:
                                update.append(node)
            for i, j in update:
                grid[i][j] = 2
            if len(visited) >= orange_amount: break
            elif new == 0:
                return -1
            res+=1
        return res