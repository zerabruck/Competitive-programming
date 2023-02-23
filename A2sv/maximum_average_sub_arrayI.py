class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summing = sum(nums[:k])
        max_sum = summing

        for end in range(k,len(nums)):
            summing -= nums[end - k]
            summing += nums[end]
            max_sum = max(max_sum , summing)

        return max_sum / k
