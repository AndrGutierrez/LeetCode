"""
ok so the space between each of the lines is 1 basically

this is a maximization problem, we can think of dp, greedy, 

i think this can be solved with dp.... no because ach one doesnt build up to the overall solution, i think this cannot be divided
into subproblems, like the solution changes each time we add smth

i think that remembering from this solution the intuition was that the maximum area is either left to right or right to left

ok so the maximum is from the longest to the longest and fartest from it 

ok so obviously the first thing is brute force, calculating all the posibilities but i **know** theres something more efficient

ok the thing is we can get the biggest left to right, and then right to left
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right =  n - 1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(area, max_area)
            if height[left] > height[right]:
                right -=1
            else:
                left +=1

        return max_area