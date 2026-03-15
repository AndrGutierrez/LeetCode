from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        word_count = Counter(words)
        n = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length*k
        answer = []

        def sliding_window(left):
            words_found = collections.defaultdict(int)
            words_used = 0
            excess_word = False

            for right in range(left, n, word_length):
                if right+word_length > n:
                    break
                sub = s[right:right+word_length]
                if sub not in word_count:
                    words_found = collections.defaultdict(int)
                    words_used = 0
                    excess_word = False
                    left = right + word_length
                else:
                    while right - left == substring_size or excess_word:
                        leftmost = s[left:left+word_length]
                        left+=word_length
                        words_found[leftmost] -=1
                        if words_found[leftmost] == word_count[leftmost]:
                            excess_word = False
                        else:
                            words_used -=1
    
                    words_found[sub]+=1
                    if words_found[sub] <=word_count[sub]:
                        words_used+=1
                    else:
                        excess_word=True
                        
                    if words_used == k and not excess_word:
                        answer.append(left)
    
        for i in range(word_length):
            sliding_window(i)

        return answer