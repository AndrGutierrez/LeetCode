# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
ith is the twin of (n-1-i)th if i <= (n/2) -1

twin sum is the sum of node and twin, return max twin

ok so the twin is like if we traversed left to right and then right to left

ok so the easiest way is having kind of an auxiliary array but even though the problem doesn't ask for an O(n) 
space complexity let't try it out

if we traverse twice we know how much n is, and if we know how much, then we 
"""
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        n = 0
        max_sum = 1
        current = head
        while current:
            nums.append(current.val)
            current = current.next

        n = len(nums)
        for i in range(n//2):
            max_sum = max(max_sum, nums[i] + nums[n-1-i])
        return max_sum