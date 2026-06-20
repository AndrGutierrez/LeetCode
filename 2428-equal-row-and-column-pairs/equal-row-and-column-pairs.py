"""
number of equal rows and columns

first is just comparing the row to each column is like O(n³) given the size of n might be possible but let's see if theres something better

but if we save each row and column separately and then compare then it's O(n²) which seems reasonable

then how do we compare... well if we use a hashmap and check it is in
"""
from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_strs = Counter()
        col_strs = Counter()
        col_aux = ['' for i in range(n)]
        res = 0
        
        for i in range(n):
            curr_row = ''
            for j in range(n):
                curr_row+=str(grid[i][j]) + ','
                # print(j)
                col_aux[j]+=str(grid[i][j]) + ','
            row_strs[curr_row]+=1

        col_strs = Counter(col_aux)
        

        for key in col_strs.keys():
            for i in range(col_strs[key]):
                if key in row_strs:
                    res+= row_strs[key]
        return res