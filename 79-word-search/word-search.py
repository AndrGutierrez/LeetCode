"""
return if word exists

ok so first of all rather than backtracking I see this might be graph dfs,
that can be also backtracking i guess

but backtracking implies we have to undo our decision, why

ok so even if its bfs or bt need a base case, 
let k=len(word)

def backtrack(path):
    if len(path) == k:
        if foundword == word: return true
        else: continue searching

    for neighbor in neighbours:
        path.append(neighbor)
        backtrack(path)
        path.pop()
        
we need to get the neighbours then, I've done this plenty of time so no need to keep reasoning
for now, lets focus on the main logic

i think were done

 
"""
from collections import defaultdict
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.res = False

        m = len(board)
        n = len(board[0])
        directions = [
            (0, -1),
            (1, 0),
            (0, 1),
            (-1, 0)
        ]

        neighbors = defaultdict(list)
        inboard = set()
        for i in range(m):
            for j in range(n):
                inboard.add(board[i][j])
                for x, y in directions:
                    row = i+y
                    col = j+x
                    if row >= 0 and col >=0 and row < m and col < n:
                        neighbors[f'{i},{j}'].append(f'{row},{col}')
        chars = set(list(word))
        for char in chars:
            if char not in inboard:
                return False
        def backtrack(path):
            if len(path) == len(word):
                foundword = ''
                for item in path:
                    i, j = item.split(',')
                    foundword += board[int(i)][int(j)]
                if foundword==word:
                    self.res = True
                    return
                return
            n = neighbors[path[-1]]
            for neighbor in n:
                if neighbor not in path:
                    path.append(neighbor)
                    backtrack(path)
                    path.pop()
        for i in range(m):
            for j in range(n): 
                if board[i][j] == word[0]:
                    backtrack([f'{i},{j}'])
                    if self.res:
                        return self.res
        return self.res