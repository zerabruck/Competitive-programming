import math
class Solution:
    def checker(self , mid , nums ):
        ele = 0
        for i in nums :
            ele += math.ceil(i/mid)
        return ele
      
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        high = max(nums)
        low = 1
        min_thr = inf
        while low <= high :
            mid = (high + low ) // 2
            if self.checker(mid, nums) <= threshold :
                min_thr = min(min_thr , mid)
                high = mid - 1

            elif  self.checker(mid, nums) > threshold :
                low = mid + 1

        return min_thr
