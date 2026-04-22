"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

recursive?

seems like,

so basically we should start dividing the grid into 4 sections and we divide each section until we get the representation

if the grid has all 0's or 1's, isLeaf=True and value is 0 or 1, all children are null

else it isnt leaf and val can be 0 or 1 doesnt matter i guess

ok so we make a recursive function

max size of grid is 64*64 so not that big, also its guaranteed to be pairs



makeGrid(section):
    allZeros = True
    allOnes = True

    division() 
    if allZeros or allOnes:
        node = Node(1 if allOnes else 0, True, None, None, None, None)
        return node


    node.topLeft = makeGrid(tl)
    node.topRight = makeGrid(tr)
    node.bottomLeft = makeGrid(bl)
    node.bottomRight = makeGrid(br)


"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def makeGrid(section):
            n = len(section)
            half = int(n/2)
            if n == 1:
                return Node(section[0][0], True, None, None, None, None)

            allZeros = True
            allOnes = True
            tl = [[0 for col in range(half)] for row in range(half)]
            tr = [[0 for col in range(half)] for row in range(half)]
            bl = [[0 for col in range(half)] for row in range(half)]
            br = [[0 for col in range(half)] for row in range(half)]

            for row in section:
                for col in row:
                    if col != 1: allOnes = False
                    if col != 0: allZeros = False
            def fill(sub_section, start_row, end_row, start_col,end_col):
                ones = True
                zeros = True

                for sub_section_i, section_i in enumerate(range(start_row, end_row)):
                    for sub_section_j, section_j in enumerate(range(start_col, end_col)):
                        val = section[section_i][section_j]
                        if val != 1: ones= False
                        if val != 0: zeros= False
                        sub_section[sub_section_i][sub_section_j]= val

                return (ones, zeros)
            fill(tl, 0, half, 0, half)
            fill(tr, 0, half, half, n)
            fill(bl, half, n, 0, half)
            fill(br, half, n, half, n)

            if allZeros or allOnes:
                node = Node(1 if allOnes else 0, True, None, None, None, None)
                return node

            node = Node(1, False, None, None, None, None)
            node.topLeft = makeGrid(tl)
            node.topRight = makeGrid(tr)
            node.bottomLeft = makeGrid(bl)
            node.bottomRight = makeGrid(br)
            return node
        return makeGrid(grid)