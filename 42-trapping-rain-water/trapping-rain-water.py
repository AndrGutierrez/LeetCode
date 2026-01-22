"""
if left <= right:
    water = max_left - left
    if left > max_left
        max_left = left
    left+=1
else:
    water = max_right - right
    if right > max_right
        max_rigt = right
    right+=1
    next
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = 0
        max_right = 0
        left = 0
        right = len(height)-1
        water = 0
        while right > left:
            print(left)
            if height[left] <= height[right]:

                if height[left] > max_left:
                    max_left = height[left]
                water+= max_left-height[left]
                left+=1
                
            else:
                if height[right] > max_right:
                    max_right = height[right]

                water+=max_right-height[right]
                    
                right-=1

            
        return water