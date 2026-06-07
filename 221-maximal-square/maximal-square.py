"""
ok so AREA of LARGEST square containing ONLY 1's

ok so first thing i can think of is brute force but that's... a lot

its like O(mnlogmn)? or something like that, because each time we try with larger squares
the amount reduces, anyway O(mn) is already a lot if the input size is like 300 each

ok so...

can we use a graph?

can we divide this into smaller subproblems?

can we use a hashmap?

we can divide it into smaller subproblems, a square is mad out of other 4 squares

we can make a new matrix that says if the square that begins in that square
is a valid square... 


"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        res = 0
        at_least_one_square_found = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    matrix[i][j] = 0
                else:
                    at_least_one_square_found = True
                    matrix[i][j] = 1

        while at_least_one_square_found:
            at_least_one_square_found = False
            res +=1
            for i in range(m):
                for j in range(n):
                    if i == m - 1:
                        matrix[i][j] = 0
                    elif j == n - 1:
                        matrix[i][j] = 0
                    else:
                        square_found = matrix[i][j] and matrix[i+1][j] and matrix[i][j+1] and matrix[i+1][j+1]
                        matrix[i][j] = square_found

                        if square_found:
                            at_least_one_square_found = True


        return int(res**2)