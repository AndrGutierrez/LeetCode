"""
Replace in place

make graph, traverse the matrix searching for the 'Os',
if already visited go next,
else do bfs, and in each node check if its in an edge,
save each node into a "current visited" (current region only)
at least one of the items in the region is in an edge, its not sorrounded
if it is,  replace in the board all the indexes, otherwise do nothing
"""

from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        self.visited = set()
        graph = {}
        for i, _ in enumerate(board):
            for j, _ in enumerate(board[i]):
                name = f'{i},{j}'
                neighbors = []
                if i > 0: neighbors.append(f'{i-1},{j}')
                if j > 0: neighbors.append(f'{i},{j-1}')
                if i < m - 1: neighbors.append(f'{i+1},{j}')
                if j < n - 1: neighbors.append(f'{i},{j+1}')

                graph[name] = neighbors
        for i, _ in enumerate(board):
            for j, _ in enumerate(board[i]):
                if board[i][j] == 'O':
                    self.bfs(graph, f'{i},{j}', board)

    def bfs(self, graph, node, board):
        q = deque([node])
        has_in_edge = False
        m = len(board)
        n = len(board[0])
        nodes = []
        while q:
            current = q.popleft()
            neighbors = graph[current]
            neighbors.append(node)
            for neighbor in neighbors:
                [i, j] = [int(item) for item in neighbor.split(',')]

                if neighbor not in self.visited and board[i][j] == 'O':


                    self.visited.add(neighbor)
                    nodes.append((i, j))
                    if i == m - 1 or j == n-1 or i == 0 or j == 0:
                        has_in_edge = True
                    q.append(neighbor)
        if not has_in_edge:
            for i, j in nodes:
                board[i][j] = 'X'