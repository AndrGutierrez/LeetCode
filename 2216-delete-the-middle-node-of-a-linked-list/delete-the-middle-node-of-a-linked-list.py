# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
delete middle node and return head, it has to be in place
"""
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 1
        current = head 

        while current.next:
            n+=1
            current = current.next

        curr = head
        half = n//2

        if n ==1 or n ==0: 
            return None
        while True:
            if not curr: break
            if not curr.next: break
            half-=1
            if half == 0:
                curr.next = curr.next.next

            curr = curr.next

        return head
            