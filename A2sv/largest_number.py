class Solution:
    def checker(self,first,second,nums):
        first_second = str(nums[first]) + str(nums[second])
        second_first = str(nums[second]) + str(nums[first])
        if first_second >= second_first:
            return first

        return second


    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            maxx = i
            for j in range(i,len(nums)):
                maxx = self.checker(maxx,j,nums)

            nums[i] , nums[maxx] = nums[maxx] , nums[i]

        if nums[0] == 0:
            return '0'

        return "".join([str(i) for i in nums])
