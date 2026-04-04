# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
k is <= n
if n % k != 0: dont reverse the remaining

says O(1), so maybe we shouldnt store into array aint doing t hat, convert to array, 
get chunks, reverse and return new linked list... though it seems to be in place

i mean you can store them into array and then change the order

traverse list, save into array, reverse the chunks, then traverse the new array,
replace the head, convert it into current

current.next = the next in the array

tough if i make a queue...
"""
# 
# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         current = head
#         q = deque([current])
#         qs = []
#         i = 0
#         while current.next:
#             i+=1
#             if i % k == 0:
#                 h = q[0]
#                 # c = h
#                 for item in q:
#                     print(item.val)
#                 #     c.next= item
#                 q= deque()
#             
#             q.appendleft(current.next)
#             current = current.next
#         if q and (len(q) / k) == 1:
#             for item in q:
#                 print(item.val)
#         elif q:
#             for item in list(reversed(q)):
#                 print(item.val)
# 

# 
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        q = deque([current])
        qs = []
        i = 0
        h = ListNode()
        c = h
        while current.next:
            i+=1
            if i % k == 0:
                for item in q:
                    c.next = ListNode(item.val)
                    c = c.next
                q = deque()
            q.appendleft(current.next)
            current = current.next
        if q and (len(q) / k) == 1:
            for item in q:
                c.next = ListNode(item.val)
                c = c.next
        elif q:
            for item in list(reversed(q)):
                c.next = ListNode(item.val)
                c = c.next        
        return h.next