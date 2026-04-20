# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
amount of numbers suggest O(n) time O(nlogn) at most

has to be height balanced bst

if it was possible to sort in less time it would

current = Node(val)

for num in nums
    if num < current

okkkk assume numbers are already sorted

it says divide and conquer but the thing is already sorted so its not sorting

these problems sometimes are recursive but this is not the case

ok so lets try dividing it


for node in nodes

5,6,7,8,9

ok it only matters that its valid and balanced, so we probably have to divide in pairs

can we take... the median?

like the number in all the middle...

-4,-3,-2,-1,2, 1000

  -2
 -3 -1
-4    2
       1000
so if we go node by node

current = num
for num in nums:
    if num > current

o but using pure logic

go to the middle, there are the same amount of elements to the left and the right

elements to the left are smaller and elements to the right are bigger, the biggest numbers are
the last ones and the smalleset are the first ones,

can i use pointers?

like if you just go to the left you will get always a subtree, so... yes thats the logic,

the middle is the starting, left to that is a subtree, and at all the right thats another subtree, and you make it into smaller subtrees

    7
  6  9
5   8

current1 = middle  
current2 = end

current1.right = end
while not all visited:
"""

from collections import deque
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None
            p = (left + right) //2
            root = TreeNode(nums[p])
            root.left = helper(left, p-1)
            root.right = helper(p+1, right)
            return root

        return helper(0, len(nums)-1)