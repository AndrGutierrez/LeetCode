import heapq
class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        heapq.heapify(heap)

        l =[]
        for lst in lists:
            if not lst: continue
            current = lst
            l.append(current.val)
            while current.next:
                current = current.next
                l.append(current.val)

        head = ListNode()     
        current = head
        l = sorted(l)

        for item in l:
            current.next = ListNode(item)
            current = current.next

        return head.next