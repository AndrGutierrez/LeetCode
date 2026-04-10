# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
traverse k nodes, reverse, traverse the rest, and keep it, make a new list

the worst case scenario is k= amount of nodes so there's no problem with just running the thing whole the whole list

theres just 100 nodes so array concatentation not a problem

pop from the q and put in the beggining
"""
from collections import deque
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        if not head: return None
        q = deque([current.val])
        while current.next:
            current = current.next
            q.append(current.val)
        
        res = ListNode()
        current = res
        k = k%len(q)
        while k > 0:
            last = q.pop()
            q.appendleft(last)
            k-=1

        for item in q:
            current.next = ListNode(item)
            current = current.next
        return res.next