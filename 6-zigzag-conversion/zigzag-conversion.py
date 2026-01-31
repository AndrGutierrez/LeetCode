"""
output: string

makes conversion depending on the number of rows

the length of the string is <= 1000 so brute force solutions might be allowed

zigzag pattern

the amount of the things in the zigzag is the number of rows-2 (it seems)

so maybe:

substring of the first three, then substring of the next two, and so on (sliding window? greedy? two pointers?)

append current+arr[space * i] until space *i >=n
current will be current_index + 1, then go back to that thing

untill all traversed

y los del medio?

no funciona

orden: baja, sube
[p] 
[a]
[y] []
[p]

make matrix

go from top to bottom until you reach nurows, then add 1 in x and 1 in y until you get back to top
repeat

you get the zigzag but how do you convert?

run on the matrix and add where you find a character

"""
import math
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        matrix = [0]*numRows
        res=""
        for i, r in enumerate(matrix):
            matrix[i] = [0]*math.floor(len(s))
        # for row in matrix:
        #     print(row)
        i = 0
        j = 0
        direction = 1
        for c in s:
            matrix[i][j] = c
            i+=direction

            if i % (numRows-1) ==0:
                j += 1
                direction*=-1

        # for i, row in enumerate(matrix):
        #     for j, column in enumerate(row):

        for row in matrix:
            for c in row:
                if c !=0: res+=c
        return res