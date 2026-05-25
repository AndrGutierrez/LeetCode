"""
ok so the operation to get the median should probably be cached on saved into an
efficient datastructure for being able to retrieve it after we insert other nums

there will be at least one element before calling findmedian

ok but I think this is pretty straightforward, we do a maxheap we dont have to sort in the beggining because
we dont have that kind of initial.

the thing would be finding the median in a maxheap without having to heapop every time you know, because even with
copies findMedian would be performed in O(nlogn) time, thoughjt that could be acceptable...

instead of that we could establish the median in every addnum, if that was possible to do in O(1) or O(log), I think it would be 
the most efficient, though the overall required seems to be O(n) or nlogn at most

because if we do the heapsort thing it will be called n times so the complexity would be O(n²logn)

the solution seems to be being able to retrieve the median in O(1) or O(logn) at most

ok so in the end the heap approach is using two heaps, a min heap with the largest elements,
and a max heap with the smallest elements

so if we pop from those heaps we always will get the median elements
"""
import heapq
class MedianFinder:

    def __init__(self):
        self.top_elements_heap = []
        self.bottom_elements_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.bottom_elements_heap, -num)
        largest_bottom_element = -heapq.heappop(self.bottom_elements_heap)

        heapq.heappush(self.top_elements_heap, largest_bottom_element)

        if len(self.bottom_elements_heap) < len(self.top_elements_heap):
            smallest_top_element = heapq.heappop(self.top_elements_heap)
            heapq.heappush(self.bottom_elements_heap, -smallest_top_element)

    def findMedian(self) -> float:
        mid1 = -self.bottom_elements_heap[0]

        if len(self.bottom_elements_heap) > len(self.top_elements_heap):
            return mid1
        else:
            mid2 = self.top_elements_heap[0]

            return (mid1 + mid2) /2 
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()