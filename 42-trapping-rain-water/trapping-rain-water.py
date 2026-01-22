"""
if left <= right:
    water = max_left - left
    max_left = max(max_left, left)
    left+=1
else:
    water = max_right - right
    max_right = max(max_right, max)
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
            if height[left] <= height[right]:
                max_left = max(height[left], max_left)
                water+= max_left-height[left]
                left+=1
                
            else:
                max_right= max(max_right, height[right])
                water+=max_right-height[right]
                right-=1

            
        return water