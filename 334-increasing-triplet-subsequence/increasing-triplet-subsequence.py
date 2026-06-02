"""
of course there's brute force, this might be a dp... but that gives us a O(n² solution at best I think, if even possible)

we can traverse the array, and look if the next number is bigger, if it isn't, we save the latest longest, and then

[99, 100, 97, 98, 95, 96, 93, 94, 1, 2, 3]

2, 1, 3, 4
i mean we only need to know if its bigger than the "smallest" tuplet

for num in nums
    if the number is bigger than the last of the smallest element an that element is part of a tuplet it means we're done, if it isnt't we add a new tuplet

if it isn't, we make it the smallest element, 
else we make another 

98, 99, 1, 2, 100
"""
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
            current_tuplet = None
            smallest = float("inf")
            for num in nums:
                if num > smallest:
                    if current_tuplet:
                        if num > current_tuplet[1]:
                            return True
                        else: current_tuplet = (smallest, num)
                    else:
                        current_tuplet= (smallest, num)
                else:
                    smallest = num
            return False