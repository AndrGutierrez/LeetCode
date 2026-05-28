"""
largest string that divides both

only uppercases.

the size of the input suggest maybe a O(n²) complexity

i can think of

ABCABCABC

ABCABC

the longest that divides both is ABC... 

we can make some kind of sliding window, take 1 char, check if we can divide, then check with 2 chars, and so on
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        i = 1
        l1 = len(str1)
        l2 = len(str2)
        res = ''

        while True:
            if l1 % i == 0 and l2 % i == 0:
                aux = str1[:i]
                contained_in_1= l1 // i
                contained_in_2 = l2 // i
                if aux * contained_in_1 == str1 and aux * contained_in_2 == str2: res =aux
            if i >= l1 or i >= l2: break
            i+=1
            
        return res