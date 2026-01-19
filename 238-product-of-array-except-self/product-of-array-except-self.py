class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        res = []

        zeros = []
        for i, num in enumerate(nums):
            if num == 0:
                zeros.append(i) 
                continue
            mult*=num
            
        if len(zeros)>=2:
            return [0]*len(nums)
        elif len(zeros)>=1:
            return [0]*(zeros[0])+ [mult] + [0]*(len(nums)-zeros[0]-1)
 
        for i, num in enumerate(nums, 1):
            if num == 0: 
                res.append(mult)
                continue                
            n = int(mult*(num**-1))
            res.append(n)
            
        return res