"""
return all possible combinations of k numbers in an n range

this asks for all combinations which can be done by brute force, the constraints of n and k size suggest that it should be at least O(n²)


so in this kind of problem we have a tree and we can decide wether take or not taking

how can we achieve this in code

ok so the combinations are unordered and cannot repeat so it seems

for number in range(1, n):
    for n2 in range(n2, n):
        res.append


but this only work for pairs, the bigger the range of things the most loops we have to do so this has to be recursive

so whats our base case

backtrack(combination):
    if len(combination) == k:
        res.append(combination)
        return
    for number in range(1,n):
        backtrack(combination + number)

so i have to not chose or undo my choice of the extra elements

"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(combination, first):
            if len(combination) == k:
                res.append(combination[:])
                return
            need = k - len(combination)
            remain = n - first + 1
            available = remain - need
            for number in range(first, first+ available+1):
                #This is basically dfs

                #decision
                combination.append(number)
                #backtracking
                backtrack(combination, number+1)
                #undo decision
                combination.pop()
        backtrack([],1)
        return res