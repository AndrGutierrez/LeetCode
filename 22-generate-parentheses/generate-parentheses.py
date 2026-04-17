"""
n pairs of parenthneses limited to 8 pairs, 16 parentheses, the low amount suggest that it could have a recursive solution, maybe backtracking

ok so we have kind of an unbalanced tree

so we have to append to the tree...

the left, the right idk

mmm since this is just brute force we might have to put all possible combinations, the decision might be opening or closing

so, if we test all possible combinations in the remaining space...

ok so test all possible combinations in remaining space by backtracking, and then we use stacks to validate like in other leetcode problems?

ok so for the simplest case where n = 1

we have these options:

()
)(
((
))

we already decided we want to brute force, so...

if we iter

()



trial 1:

((
()

backtrack
))
)(

how do i make the decision

how was the stack validation again?

()
(())
))))
()))
"""
from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res= []
        total =  n*2
        select = {
            "(": ")",
            ")": "("
        }
        def backtrack(curr):
            if len(curr) == total:

                res.append(curr[:])
                return
            for i in range(2):
                if i == 0:
                    parentheses = '('
                else:
                    parentheses = ')'
                curr+=parentheses
                backtrack(curr)
                curr = curr[:-1]
        backtrack('(')
        finalres = []
        for r in res:
            q = deque()
            valid = True
            for c in r:
                if c == '(':
                    q.append('(')
                if c == ')':
                    if len(q) == 0:
                        valid = False
                        break
                    else:
                        q.pop()
            if len(q) ==0 and valid:
                finalres.append(r)

        return finalres