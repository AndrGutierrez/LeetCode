"""
lowercase english letters only

return if we can make a palindrome performing one or two operations

for 0 operations is it false too?

operation is changing character

normally for checking palindromes we just use two 

by brute force it would be changing 1 character to anything and then checking if it's palindrome for each character so not very
efficient. scales too fast

well first of all we can divide the word into two and check how many letters are equal, we have to taking into account odd number of c

so we just traverse the array using two pointers until we get to the half, and check on each index if the...

ok so if it's exactly two operations... I'm gonna assume it's not valid to perform it twice on the same c...

if it requires 0 it can also require two you know, so we can keep going with the same plan
"""
class Solution:
    def makePalindrome(self, s: str) -> bool:
        n = len(s)
        half = (n // 2)
        diff = 0
        for i in range(half):
            if s[i] != s[n-i-1]:
                diff+=1
        if diff <=2 : return True
        return False