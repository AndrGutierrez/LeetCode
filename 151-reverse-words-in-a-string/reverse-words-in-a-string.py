from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        left = 0
        right = 0
        current_word = ''
        q = deque()
        res = ''
        while right < n:
            current_word = ''
            while s[right] != ' ' and right<n:
                current_word+=s[right]
                right+=1
                if right > n-1:  break
            if current_word != '':
                if res == '': res = current_word
                else: res = f"{current_word} {res}"
            right+=1


        return res