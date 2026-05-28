class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)

        i = 0
        res = ""
        while True:
            if i < l1:
                res += word1[i]
            if i < l2:
                res += word2[i]
            if i >= l1 and i >= l2: break
            i+=1
        return res 