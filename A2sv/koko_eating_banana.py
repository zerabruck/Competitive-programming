import math
class Solution:
    def checker(self , mid , piles):
        count = 0
        for ele in piles :
            val = math.ceil(ele / mid )
            count += val

        return count
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1 
        high = max(piles)
        k = inf

        while low <= high :
            mid = (high + low) // 2

            if self.checker( mid , piles) > h :
                low = mid + 1 
            elif self.checker( mid , piles) <= h :
                k = min ( k , mid)
                high = mid - 1

        return k
