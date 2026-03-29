"""
return *minimum* *window substring* 
such that *every* character in *t* is included in the window (including duplicates)

if theres not return ""

the answer is unique

there's probably a brute force solution, but the size of the input suggest a O(n)

s might be the same size as t

make pointer, if 

ok so left pointer checks if is in letters and > 0
if it is, substract 1, move the right pointer until we find a solution and add to the solution list if shorter than last solution
end when reached the end of the array 

yes this is sliding window not two pointers

ok so move right until completing, then move left 

make a hashmap with appearences and pop until the appearences of each of t's leter is not the correct
"""
from collections import Counter
import math
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        letters = Counter(t)
        appearances = defaultdict(int)
        required = len(letters)
        left = 0
        right = 0
        formed = 0
        res = ""
        ans = (math.inf, None, None)
        while right < m:
            c = s[right]
            appearances[c]+=1
            if(c in letters and appearances[c] == letters[c]):
                formed+=1
            while left <= right and formed == required:
                c = s[left]
                window_size = right-left+1
                if window_size < ans[0]:
                    ans = (window_size, left, right)
                
                left+=1
                appearances[c]-=1

                if (c in letters and appearances[c] < letters[c]):
                    formed -=1
            right+=1
        return "" if ans[0] == math.inf else s[ans[1]:ans[2]+1]