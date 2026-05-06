"""
check if number is palindrome,
since it's very big probably O(n) is too much, maybe constant time using math or at least O(n/2)

how do we know if a number is palindrome................

performing basic operations doesnt seem to be the case, two pointers? that at least is O(n/2) but no for this size that optimization is worthless

single digit are expected to be palindromes

if we sum elements at left and elements and right it should be the same, is there a possible way where this is... i dont think so well yes

3 1 2 3 1

well i can make a hashmap?

no, well of course i can but no

of course im an idiot, 
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        string = str(x)
        index = len(string)//2

        if len(string) % 2 == 0:
            end = index
        else: end = index+1
        return "".join(reversed(string[:end])) == string[index:]