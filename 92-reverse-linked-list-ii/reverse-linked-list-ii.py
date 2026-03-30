# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
amount is total-left-right
its just a few nodes so we can traverse several times

get total by traversing the whole thing, get the amount of nodes... says one pass, well idc

now do it again until left, 
begin from head and go next until left is 0, go until the amount is 0, save into array, build linked list from the collected

its 1 indexed i think
"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current= head
        items = []
        items.append(current.val)

        while current.next:
            current = current.next
            items.append(current.val)
        head = items[:left-1]
        tail = items[right:]

        reverse = list(reversed(items[left-1:right]))

        full = head +reverse+tail
        h = ListNode(full[0])
        current = h
        for item in full[1:]:
            current.next = ListNode(item)
            current = current.next
        return h
