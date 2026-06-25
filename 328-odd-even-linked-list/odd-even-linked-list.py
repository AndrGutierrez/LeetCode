# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
return evens and odds in place

we can maybe try to swap

make kindof a pointer like last odd and last even, so we just move the place
"""
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        odd = head
        even = head.next
        firsteven = even
        curr = head

        while True:
            if not curr or not curr.next: break
            odd.next = odd.next.next
            if odd.next:
                odd = odd.next
            if even.next:
                even.next = even.next.next
                if even.next:
                    even = even.next
                curr = curr.next

        odd.next = firsteven
        return head