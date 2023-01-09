class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        postive = [ i for i in nums if i > 0]
        negetive = [i for i in nums if i <0 ]
        rearranged = [0] * len(nums)
        even_count = 0
        for i in postive:
            rearranged[even_count] = i
            even_count += 2
        negetive_count = 1

        for i in negetive:
            rearranged[negetive_count] = i
            negetive_count += 2

        return rearranged

                    



