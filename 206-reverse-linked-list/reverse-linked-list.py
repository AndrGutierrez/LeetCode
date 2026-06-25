# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
return reversed list inplace

"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        curr = head
        nums = [curr.val]
        while curr.next:
            curr = curr.next
            nums.append(curr.val)
        headres = ListNode(nums[-1])
        curr = headres
        for num in list(reversed(nums))[1:]:
            curr.next = ListNode(num)
            curr = curr.next
        return headres