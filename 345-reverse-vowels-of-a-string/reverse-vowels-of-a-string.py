"""
can be upper or lowercase

reverse the vowels,

printable ascii characters

register the vowels in an array, thentraverse the reversed array, and if you find a vowel pop  
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels= set(['a','e','i','o','u'])
        registered = []
        res = list(s)
        for c in s:
            if c.lower() in vowels:
                registered.append(c)

        for i, c in enumerate(s):
            if c.lower() in vowels:
                res[i] = registered.pop()

        return "".join(res)