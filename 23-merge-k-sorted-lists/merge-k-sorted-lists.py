# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
merge into sorted

ok so there can be lots of linked list so this probably has to be O(n) or less

lists are already sorted

mmm heaps might be handy

we could insert into a heap, and then convert? no that's heapsort and thats nlogn

lists might be different sizes

can we do some kind of three pointer approach? maybe too much, is there a way to reduce to logn?

no, we cannot use pointers(?) this is a linked list... though converting list to array might not be that hard

I mean i think the minimum time we can get for this is O(nk)

if we change the dimension?

like
1 4 4

1 3 5

2 6
"""

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)

        l =[]
        for lst in lists:
            if not lst: continue
            current = lst
            heapq.heappush(heap, current.val)
            while current.next:
                current = current.next
                heapq.heappush(heap, current.val)
        head = ListNode()     
        current = head
        for i in range(len(heap)):
            current.next = ListNode(heapq.heappop(heap))
            current = current.next

        return head.next