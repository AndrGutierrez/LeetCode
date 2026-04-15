"""
return all permutations in any order

numbers can be negative, maximum of 6 numbers wich suggest this needs an exhaustive search approach

probably backtracking

so 

lets define a base case

got o number n, we can pick any of the other numbers, and we have to pick one, and recursively pick the others, so theres a posibility for each decision we take like the tree I drew

so we have to do inorder traversal

def backtrack(current, numbers):
    if len(current) == len(nums):
        res.append(current)
    for i in range(numbers):
        
        current.append(number)
        backtrack(current, numbers[i+1:])
        current.pop(number)
maybe we have to backtrack the options not the number itself, because we have to try all the other remaining options but...

swap the tree?

maybe the tree approach is better it will take more time but i think its

maybe i can do more of a bfs
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(current):
            if len(current) == len(nums):
                res.append(current[:])
                return
            for i in range(len(nums)):
                number =  nums[i]
                if number not in current:

                    current.append(number)
                    backtrack(current)
                    current.pop()
        backtrack([])
        return res