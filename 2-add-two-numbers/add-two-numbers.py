# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#didnt tell me to assume it fits in an i32 so of course i should have solved there was an overflow issue
from collections import deque
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 =deque()
        arr2 =deque()

        current = l1
        while current:
            arr1.appendleft(current.val)
            current = current.next
        
        current = l2
        while current:
            arr2.appendleft(current.val)
            current = current.next

        res = ''
        carry = 0
        
        head = ListNode(None)
        current = head
        while arr1 or arr2:
            n1 = 0
            n2 = 0
            if arr1:
                n1 = arr1.pop()
            if arr2:
                n2 = arr2.pop()
            r = n1 + n2 + carry
            if r >= 10: 
                carry = 1
                r = str(r)[-1]
            else: carry = 0
            
            res+=str(r)
            
            node = ListNode(int(r))
            current.next = node
            current = current.next
            # if not head:
            #     head = node
            #     current = head
# 
            # current.next = node
            # current = current.next
            
        if carry!=0: current.next = ListNode(1)
        return head.next
