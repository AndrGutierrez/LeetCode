"""
ok, an optimization problem

we cannot rob two adjacent houses

this could be dp, can we divide it into smaller subproblems?

for example

[1, 2, 1000, 1002]

[1, 2, 1001, 1004]

I mean can we just make this the sum of the evens and sum of the odds? 

is there a case where we cant do that??

rigt cases like

[2, 1, 1, 2]

or even more extreme stuff i guess

[1, 300, 1, 3, 100]

where it's better to pick just the two 

so what we do is... well the input size of nums suggest maybe a O(n²), brute force is something crazy exponential
but I think O(n²) is manageable, and if it isnt it might lead to a more efficient solution

[1, 300, 2, 303, 400]

so filling the last one in this case... i mean we just gotta get the biggest so far 
that isn't adjacent to the current and sum what we have, or is there something better?

and if it isn't better? it has to be by definition so...
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        res = []
        if len(nums) == 1: return nums[0]
        for i in range(len(nums)):
            if i == 0 or i ==1:
                res.append(nums[i])
            else: 
                res.append(max(max(res[:i - 1]) + nums[i], res[-1]))
        return max(res[-1], res[-2])