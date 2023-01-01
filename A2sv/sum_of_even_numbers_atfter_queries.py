class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sums = sum(i for i in nums if i % 2 == 0)
        result=[]
        
        for value,index in queries:
            if nums[index] % 2 == 0 :
                sums -= nums[index]

            nums[index] += value

            if nums[index] % 2 ==0:
                sums +=nums[index]

            result.append(sums)

        return result
