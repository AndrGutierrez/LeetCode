"""
0 indexed

return maximum number of books you can take

books[i], number of books in the ith shelf of the bookshelf

we can take strictly fewer books from shelf i, than what we take from                                       
shelf i + 1

we can only take from a contiguous section

input size suggest O(n) or O(nlogn) at most

ok so this sounds like dp, to check that we can think first of the recursive solution

check all possible cases with recursion, can we divide this into smaller subcases?

yeah...

so it is important that we run this from left to right 

[8, 8, 8, 10]

though this is not a take or not take decision, theres more nuance to it

I think using a heap would work, it would be like

res = 0

make a maxheap this way (i, val)

while heap:
    index, item = pop()
    if index ==  last_index -1:
        res+=item
    elese:
        res = max(res, item)

no this approach doesnt work because of the first example, look at how we use 5....

though we can store that into a queue?

and then we pop from the queue the next biggest

no i think it doesnt work,


"""
from collections import deque
class Solution:
    def maximumBooks(self, books: list[int]) -> int:
        n = len(books)
        def calculateSum(l, r):
            cnt = min(books[r], r-l + 1)
            return (2*books[r] - (cnt -1)) * cnt //2
        
        stack = []
        dp = [0] * n

        for i in range(n):
            while stack and books[stack[-1]] - stack[-1] >= books[i] - i:
                stack.pop()
            
            if not stack:
                dp[i] = calculateSum(0, i)
            else:
                j = stack[-1]
                dp[i] = dp[j] + calculateSum(j + 1, i)
            stack.append(i)
        return max(dp)