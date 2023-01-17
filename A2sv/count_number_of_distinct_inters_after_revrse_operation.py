class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums_set = set()

        for num in nums:
            nums_set.add(num)
            string_num = str(num)
            string_reversed = string_num[::-1]
            nums_set.add(int(string_reversed))

        return len(nums_set)