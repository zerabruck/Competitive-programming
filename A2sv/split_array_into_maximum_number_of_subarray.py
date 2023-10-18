class Solution:
    def maxSubarrays(self, arr):
        result = 0
        count = 0
        for element in arr:
            if result == 0:
                result = element
            else:
                result = result & element
            if result == 0:
                count += 1
        return max(1, count)
