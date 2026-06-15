"""
ok so sliding window
"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left=0
        right=0
        n = len(nums)
        curr = 0
        res = 0
        delete_used = False
        all_ones = True
        while right < n:
            print(left, right)
            if nums[left] == 0:
                left+=1
                right = max(left, right)

                all_ones = False
                continue
            if nums[right] == 1:
                curr+=1
                right+=1
            else:
                all_ones = False

                if delete_used:
                    while nums[left] != 0:
                        left+=1
                        curr-=1
                    right = max(left, right)

                    delete_used = False
                else:
                    right+=1
                    delete_used = True

            res = max(res, curr)
        if  all_ones: res-=1
        return res