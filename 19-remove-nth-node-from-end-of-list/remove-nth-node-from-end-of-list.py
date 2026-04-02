# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
fairly small
I suppose it has to be in place
says in one pass but...
save the nodes into a hashmap with number, get the amount, then substract and remove that one
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current= head
        nodes = []
        while current:

            nodes.append(current)
            current = current.next
        if len(nodes) == 1: 
            return None

        amount = len(nodes)
        beforeReplace = amount - n -1
        afterReplace = amount - n +1
        if beforeReplace < 0:
            return head.next
        if afterReplace >= amount:
            nodes[beforeReplace].next = None
        else:
            nodes[beforeReplace].next = nodes[afterReplace]
        return head