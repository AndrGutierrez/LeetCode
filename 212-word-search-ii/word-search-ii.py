"""all the words from the array on the board

i know this is a trie excercise but lets pretend i dont know it

same cell may not be used more than once so for example

o o
o d

[oodoo] cannot though there's some kind of loop

though now that i know the trie it seems obvious, make the trie with the neighbors and search

so

make trie

how do i fill it


trie = 

for row in board
    for item in row:
        neighbor is top and the neighbor of that is top

mmm whats the best way to fill it

it also goes backwards

ok start from 0,0, make each adjacent a neigbhor and convert every adjacent you know, but backwards...

just make each one a trie, then traverse for each and search

ok so the solution is make a trie and then search witht the neighbors inside of it,
but the thing is we dont have to always start from the same so maybe we can pass the node 
to search...

what we have to do is to look for a word, so if we get to a leaf well we're done

so run the search of the trie until we reach a leaf or none of the children has children

some kind of bfs?

traverse board

if current is in trie:
    check if any of current neighbor's is its child in the trie
    if there, add them to a queue, and do bfs until reaching a leaf,
    if leaf found, word found 
"""

class TrieNode:
    def __init__(self):
        self.isLeaf = False
        self.children = [None] * 26
        self.word = None
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.root.children = [None] * 26
    def insert(self, word):
        current = self.root
        for c in word:
            index = ord(c) - ord('a')
            if current.children[index] is None:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.result = []
        nodes = defaultdict(TrieNode)
        self.m = len(board)
        self.n = len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        for row in board:
            print(row)
        for i in range(self.m):
            for j in range(self.n):
                if trie.root.children[ord(board[i][j]) - ord('a')]:
                    self.backtracking(i, j, trie.root)
        return self.result

    def backtracking(self, row, col, parent):
        c = self.board[row][col]
        index = ord(c) - ord('a')
        current = parent.children[index]
        if current.word is not None:
            self.result.append(current.word)
            current.word = None

        self.board[row][col] = '#'
        offsets = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for i in range(4):
            newRow = row + offsets[i][0]
            newCol = col + offsets[i][1]
            if newRow < 0 or newCol < 0 or newRow >= self.m or newCol >=self.n:
                continue
            else:
                c2 = self.board[newRow][newCol]
                if c2 == '#': continue
                index2 = ord(c2) - ord('a')
                if current.children[index2]: 
                    self.backtracking(newRow, newCol, current)
        self.board[row][col] =c