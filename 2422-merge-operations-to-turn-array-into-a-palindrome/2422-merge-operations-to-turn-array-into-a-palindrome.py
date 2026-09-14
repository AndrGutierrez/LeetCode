"""
replace the su adjacent elemets with sum

all numbers are positive

return minimum operations to get a palindrome

minimum, we can think of dp maybe as an optimization but let's see, I don't think so

size of the input suggest O(n), O(nlogn) at most...

palindrome..............

ok so to know if it's a palindrome themost efficient way is using two pointers so we get it in O(n) time

if we start in the center

we can also do the "squash" operation n-1 times I think

maybe thinking about dividing the array into a left and a right part

ok I see the two pointers now i think
"""
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) -1
        res = 0
        
        left = nums[lo]
        right = nums[hi]

        while hi > lo:
            if left > right:
                hi-=1
                right += nums[hi]
                res+=1
            elif right > left:
                lo+=1
                left += nums[lo]
                res+=1
            else:
                hi -=1
                lo +=1
                left = nums[lo]
                right = nums[hi]
        return res