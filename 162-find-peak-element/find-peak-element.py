"""
find peak element and return the index, so it's the number that is greater than both neighbors

this is binary search but first i think of two pointers but that's O(n) so its discarded

the order is random

if the item right to the first element is smaller, first element is peak

if the element left to last element is smaller, last element is peak    

binary search only works if it's sorted...
 
i mean what is sorted is the x axis

butttttt we only need one peak, the worst case is repeating peaks i think but in that case , i gues it 
is guaranteed to have at least one peak, so we can assume that if there's a bigger number theres a peak towards there?   
not necessarily

if  i go the wrong way the time complexity should be something like n/2*logn wich is nlogn so no, i also need something to look for

i mean a peak is basically a place where the slope is 0 but i dont thing thats gonna be useful here

well first we can check if the last is bigger than the first, in that case the peak is the last

else the peak is the first

well if its not any of those cases there has to be a peak in the middle (if there is)

ok so there cannot be equal numbers following  

ok now that we occupied the special cases we only have to care about the case

nums[1] > nums 0 and nums[-2] > nums[-1] which implies theres a peak in the middle at least, so we can search

if the number is the solution return index

if the number is bigger than the last one theres a  solution is in the right side, if it is smaller theres a solution in both sides i think


"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int: 
        if len(nums) == 1: return 0
        if nums[0] > nums[1]: return 0
        if nums[-1] > nums[-2]: return len(nums)-1

        high = len(nums)-1
        low = 0

        while high >=low:
            mid = low+(high - low)//2
            print(mid)
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                low = mid
            else:
                high = mid