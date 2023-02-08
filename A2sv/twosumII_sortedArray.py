class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        beg = 0
        end = len(numbers) - 1

        while beg <= end :
            summed = numbers[beg] + numbers[end]
            if summed > target:
                end -= 1
            elif summed < target:
                beg += 1
            else:
                return [beg + 1 , end + 1]


