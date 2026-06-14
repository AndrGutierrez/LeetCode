"""
maximum number of vowels in a substring k

ok this is obviously sliding window, the problem is that if i just make the calculation each time it is  O(nk)

so what i have to do is keep the length of the current window, remove the last, if it was a vowel substract, 
and then the new added add if its a vowel and return the maximum
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        n = len(s)
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        for i in range(k):
            if s[i] in vowels:
                res +=1
        
        latest = res
        

        for i in range(n-k):
            if s[i] in vowels:
                latest-=1
            if s[i+k] in vowels:
                latest +=1

            print(s[i], s[i+k])
            res = max(latest, res)
        return res