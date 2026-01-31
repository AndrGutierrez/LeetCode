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

ok every one has its thing associated with a number,
if i make list of tuples witht he number and the other, what do i do

sorting is better than this, but still worse


"""
import math
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res=""
        i = 0
        # j = 0

        dic = {}
        direction = 1
        for c in s:
            if dic.get(i):
                dic[i].append(c)
            else: dic[i] = [c]

            i+=direction
            if i % (numRows-1) ==0:
                # j += 1
                direction*=-1

        for val in dic.values():
            for c in val:
                res+=c
        return res

