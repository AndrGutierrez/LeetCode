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
        if not head: return None

        slow = head
        if not slow.next: return None
        fast = head.next.next
        while True:
            if not fast or not fast.next: break
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
