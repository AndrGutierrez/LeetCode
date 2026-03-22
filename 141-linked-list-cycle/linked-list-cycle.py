# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
not necessarily unique

says can be solved in O(1)... MEMORY

ok so you cannot just go until repeated because vals of this are not unique...
we could assign an id to each 1 but asks for O(1) memory and...
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool: 
        if not head: return False 
        visited = set()
        current = head
        while True:
            current = current.next
            if not current: return False
            if current not in visited:
                visited.add(current)
            else: return True
        return False
                