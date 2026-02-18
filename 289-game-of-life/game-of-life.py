"""
if alive:
    neighbors < 2 dies
    2 <= neighbors <= 3 lives
    neighbors > 3 dies
if dead:
    if neighbors == 3: revive

deaths occur at the same time

given the current state, update to next

in place (probably need to save memory)

m and n at least 1, maximum 25

traverse the matix, save in a hashmap the amount of alive neighbors and then traverse the array again and update


"""
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        neighbormap= [[0 for col in range(n)] for row in range(m)]
        # print(neighbormap)
        for i, row in enumerate(board):
            for j, column in enumerate(row):
                left = j -1
                right = j+2

                top = i-1
                bottom= i+2

                if left < 0: left = 0
                if top < 0: top = 0

                if bottom > m: bottom = m
                if right > n: right = n

                alive_neighbors = 0
                for k in range(top, bottom):
                    for l in range(left, right):
                        if (k != i) or (j != l):
                            alive_neighbors += board[k][l]

                neighbormap[i][j] = alive_neighbors
                
        for i, row in enumerate(board):
            for j, column in enumerate(row):
                alive_neighbors = neighbormap[i][j]
                is_alive= board[i][j]
                if is_alive:
                    if alive_neighbors < 2 or alive_neighbors > 3: board[i][j] = 0
                elif alive_neighbors == 3:
                    board[i][j] = 1