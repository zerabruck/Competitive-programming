class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        result = 0
        for index in range(31, -1, -1):
            prefixs = set([num >> index for num in nums])
            result <<= 1
            candidate = result + 1
            for p in prefixs:
                if candidate ^ p in prefixs:
                    result = candidate
                    break
        return result
