class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        minimo = min(nums)
        maxo = max(nums)
        add = min(maxo - minimo, k)
        minimo += add
        sub = min(maxo - minimo, k)
        maxo -= sub
        return maxo - minimo     
