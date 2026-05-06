"""
number of trailing zeros, calculating the number would probably be too hard

if the problem was only if it has a zero 

well if theres any zero it wouldnt disappear so if we find one, we could go from 
right to left if needed, but dont think thats the case

mmmmmmmmmmm is there anything more efficient than O(n)? lests try O(n) first
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        fact = n
        if n == 0: return 0
        for i in range(n-1, 0, -1):
            fact = fact*i
        
        res= 0
        while fact % 10 ==0:
            res+=1
            fact = fact//10
        return res