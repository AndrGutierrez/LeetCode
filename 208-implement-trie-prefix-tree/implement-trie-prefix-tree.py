class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False
class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.root.children = [None] * 26

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                new_node = TrieNode()
                curr.children[index] = new_node
            # curr.isLeaf=False
            curr = curr.children[index]
        curr.isLeaf =  True

    def search(self, word: str) -> bool:
        curr = self.root
        equals = True
        for c in word:
            index = ord(c) - ord('a')
            # print(index, curr)
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.isLeaf

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        starts_with = True
        for c in prefix:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                starts_with = False
                break

            curr = curr.children[index]
        return starts_with


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)