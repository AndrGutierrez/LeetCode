"""
its sorted

it's possibly left rotated at some arbitrary index k >=1

all vlues are unique

we have to search for a value so it could be binary search

if we want to know at which index it is rotated thats O(n) so no

but if we could separate the problem into two different arrays then we could binary search

i mean we could search which element is smaller than it's left neighbor and then get it and do binary search on both

but for that we need a criteria of which side to chose and i dont think we can get that sunce

[3,4,5,6,7,8,9,10,11,12,0,1,2] for example at the middle we have no way to know the way to go

but dont forget we're searching for a number so... its the same? the thing is, we're not sure if it's rotated

if we know the array is rotated then we know which side to look for

well if last item is smaller than the first we know is rotated for sure

but we dont know at which index it might be completely rotated

well if we evaluate at the middle we can make sure that it is rotated until that point, do we need to do it on each iteration?

if the the middle element is grater than the right element it is rotated at least until that point, so then we can chose to which side we
can direct the search for, the criteria for the binary search however depends on wether the side we're searching in is rotated or not

[99, 100, 1,2,3,4,5,6,7,8]

but we can always compare the mid element to the first element
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1: return 0 if target == nums[0] else -1

        rotated = False
        if nums[0] > nums[-1]:
            rotated = True
        if not rotated:
            return self.binary_search(nums, target, 0)
        high = len(nums)-1
        low = 0
        rotated_index = -1

        while high >= low:

            mid = low + (high-low)//2
            if nums[0] == nums[mid]:
                rotated_index = mid + 1
                break
            if nums[0] > nums[mid]: 
                if nums[mid-1] > nums[mid]:
                    rotated_index = mid
                    break
                else:
                    high= mid -1

            else:
                low = mid+1
        print(rotated_index)
        is_in_left = self.binary_search(nums[:rotated_index], target, 0)
        is_in_right= self.binary_search(nums[rotated_index:], target, rotated_index)

        if is_in_left != -1: return is_in_left
        elif is_in_right !=-1: return is_in_right
        else: return -1

    def binary_search(self, arr, target, starting_index):
        high = len(arr)-1
        low = 0

        while high >= low:
            mid = low + (high-low)//2
            if arr[mid] == target:
                return starting_index + mid
            if arr[mid] > target: 
                high = mid -1
            else:
                low = mid + 1
        return -1