"""
operations:

-swap
-replace ALL ocurrences of EXISTING chars to other EXISTING chars

and the question is if we can conbert word1 into word2 using these operations

ok for the replacement operation then we can check if the char in word2 is in word1 and that would be eligible

can we divide this into smaller subproblems? doesnt seem the case
can we model this into a graph? doesnt seem the case

we could maybe use two pointers but

lets see, if we traverse word1,  and word2, i mean if they have the same chars isn't it possible?

the only thing i can think of where this isnt the case is some kind of intermediate state

abcde eeeee

i think it should be possible i have no proof but idk

mmmmm if they got the same amount of stuff its just matter of swapping, so if thats true it should be true

if it isnt, it still can be done replacing, we can check what are the differences, if what we need to replace to is in the string, and if after that
replacement we can move on, then check again until....... the amount to replace is different?

so if we replace all these will we get the same amount of what we're looking for?

if we remove the matches and just stay with a string that has the diff...............

oks so if there's a diff there should be the same amount of differences like
   word1  word2
a  3      2
b  2      1
c  1      3

like if the columns are the same there must be a way to be rearranged, we can sort but we can also check that it exists and not sort
"""

from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        s1 = Counter()
        s2 = Counter()
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        if counter1 == counter2: return True
        for c1 in counter1.keys():
            if counter1.get(c1) != counter2.get(c1):
                if counter1.get(c1): s1[counter1.get(c1)]+=1 
                if counter2.get(c1): s2[counter2.get(c1)]+=1


        return s1==s2