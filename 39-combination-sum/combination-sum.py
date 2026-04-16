"""
all possible **unique** combinations that sum to target, including if its the same number, but the same number can be repeated indefinitely 

very important, candidates are all opsitive

contstraints suggest this is a backtracking problem, two combinations are unique if the frequency of at least one number is different

less than 150 combinations

ok so the size is fairly small so brute force and recursion might be an option

so probably backtracking

sorting candidates might be useful, and probably wont impact on performance

ok so

if sum(current) > 7:
    return
if sum(current) == 7:
    res.append(current[:])
    return 
for c in candidates:
    current.append(c)
    backtrack(current)
"""

from collections import Counter
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res =[]
        solution_ocurrences = []
        def backtrack(curr):
            s = sum(curr)
            if s > target: return
            if s == target:
                ocurrences = Counter(curr)
                if ocurrences not in solution_ocurrences:
                    solution_ocurrences.append(ocurrences)
                    res.append(curr[:])
                #res.append(curr[:])

                return
            for c in candidates:
                curr.append(c)
                backtrack(curr)
                curr.pop()
        backtrack([])
        return res