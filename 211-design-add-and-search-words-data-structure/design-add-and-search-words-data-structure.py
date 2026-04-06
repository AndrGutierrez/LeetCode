"""
implement a trie

when initializing, create an initial node, then add the letters as neighbors

to search you have to do dfs, interpret point as any

#### inserting:
set root as current char

for each char in word:
    if not already in current's neighbors
        add char to neighbors
        set new char as current
    else:
        set neighbor as current

### search
set root as current char
for each char in word:
    if in current's neighbors:
        continue
    elif is a dot:
        do bfs
    else: continue
"""
from collections import deque
class GraphNode:
    def __init__(self):
        self.children = [None] *26
        self.isLeaf = False

class WordDictionary:

    def __init__(self):
        self.root = GraphNode()
        

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            index = ord(c)-ord('a')
            if current.children[index] is not None:
                current = current.children[index]
            else:
                current.children[index] = GraphNode()
                current = current.children[index]
        current.isLeaf= True
    def search(self, word: str, provided_current=None) -> bool:
        current = provided_current if provided_current else self.root
        for i, c in enumerate(list(word)):
            if c != '.':
                index = ord(c)-ord('a')
                if current.children[index] is None:
                    return False
                current = current.children[index]
            else:
                for child in current.children:
                    if child is not None:
                        found = self.search(word[i+1:], child)
                        if found: return True
                return False
        return current.isLeaf
            # else:
            #     q = deque([child for child in current.children if child is not None])
            #     while q:
            #         aux_c = q.popleft()
            #         index= ord(aux_c) - ord('a')
            #         current.children[index]

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)