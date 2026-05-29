class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        curr = ""
        for c in s:
            if c.isalnum():
                curr+=c
            else:
                if curr is not '':
                    words.append(curr)
                curr = ''            
        if curr is not '':
            words.append(curr)
        return " ".join(list(reversed(words)))