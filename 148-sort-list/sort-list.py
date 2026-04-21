# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
sort ascending
"""
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        aux = []
        if head is None: return None
        current = head
        aux.append(current.val)
        while current.next:
            current = current.next
            aux.append(current.val)

        aux = sorted(aux)

        res = ListNode(None)
        current = res
        for item in aux:
            current.next = ListNode(item)
            current = current.next
        return res.next