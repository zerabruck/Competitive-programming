class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pre_sum = [0]
        for num in nums:
            pre_sum.append(pre_sum[-1] + num)
        min_len = 0
        end = 1
        for start in range(1,len(pre_sum)):
            sums = pre_sum[start] - pre_sum[end - 1]
            while sums >= target and end <= start:
                if min_len == 0:
                    min_len = (start - end) + 1
                else:
                    min_len = min(min_len , (start - end) + 1)
                end += 1
                sums = pre_sum[start] - pre_sum[end - 1]

        return min_len
