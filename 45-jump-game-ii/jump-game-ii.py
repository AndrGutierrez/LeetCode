from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1: return 0

        end = 0
        start = 0
        jumps = 1
        jumps_arr =deque()
        jumps_arr.append(end)
        for i, num in enumerate(nums):
            print(i, jumps, jumps_arr)
            if end >=len(nums)-1: break
            
            if i>jumps_arr[0]:
                jumps+=1
                jumps_arr.pop()
                jumps_arr.append(end)

            if i+num >= end:
                
                start=end
                end = i+num

            
                
        return jumps