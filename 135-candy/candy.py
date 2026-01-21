class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left_to_right = [1] * n
        right_to_left = [1] * n
        for i, r in enumerate(ratings[:n-1]):
            ri = n-1-i
            if ratings[i+1] > ratings[i] :
                left_to_right[i+1] = left_to_right[i]+1
            if ratings[ri-1] > ratings[ri]:
                right_to_left[ri-1] = right_to_left[ri]+1

        res = 0                                                          
        for i,_ in enumerate(ratings):
            res+=max(left_to_right[i], right_to_left[i])
        return res