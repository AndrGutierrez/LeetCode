"""
items in rows are sorted
ok also the matrix is sorted so we just have to flatten it and do binary search... but merging arrays is maybe a lot of computing? well we can do binary search individually so...?

well we can do binary search first in columns and then in rows
search for target in O(logn)

ok so the most efficient way to do this is binary search

we can search in columns first and then in rows i think...

lets say

1 100
2 10
3 50

so we have to build the way to do this but i would just be traversing the array
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix)
        in_rows = -1
        while low <= high:
            mid = low + (high-low)//2
            if mid < len(matrix):
                if matrix[mid][0] == target:
                    return True
                elif matrix[mid][0] < target:
                    low = mid +1

                else:
                    high = mid-1
            else:
                high =mid-1
        else:
            row = low-1
            low = 0
            high = len(matrix[0])
            while low <= high:

                mid = low + (high-low)//2
                if mid < len(matrix[0]):

                    if matrix[row][mid] == target:
                        return True
                    elif matrix[row][mid] < target:
                        low = mid +1
                    else:
                        high = mid-1
                else:
                    high = mid-1
        return False