"""
remove x and y where x + y == y

nums are all positive

brute force is something like: 

compare the first element with each other element and check if equals, if not go to next element and repeat the process, that's O(n²)

how many times can i do that, ok  

ok can we use dp? i dont think this can be divided into smaller subproblems since we alter the array each time

can we use a graph or a hashmap? doesnt seem that kind of problem

we could sort and then... nah...? well at least it's an option if i dont find anything better

if it was sorted
if we use two pointers, one at the beggining, and other at the end, if the sum differs from k we can move the pointers in a range that
will always help us to find the solution, well let's try it out it doesnt seem that hard

also if we remove that's O(n time so we would need to swap and sort each time... no, we dont need to remove
"""
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        res = 0
        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            if nums[left] + nums[right] > k:
                right-=1
            elif nums[left] + nums[right] < k:
                left+=1
            else:
                res+=1
                right -=1
                left +=1

        return res
        