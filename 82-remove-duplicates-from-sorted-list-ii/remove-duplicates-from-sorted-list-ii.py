# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
remove duplicates, doesnt have to be in place, list guaranteed to be sorted but

i can traverse the list until the number changes and change the next
"""
from collections import deque
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        current = head
        last_number = current
        q = deque()
        appearances = defaultdict(int)
        appearances[current.val]+=1

        while current.next:
            current = current.next
            appearances[current.val]+=1


        h2 = ListNode()
        current = h2
        for key in appearances.keys():
            if appearances[key] <2:
                current.next = ListNode(key)
                current = current.next
        return h2.next