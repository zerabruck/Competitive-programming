class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1]
        backward = [1]

        for index,num in enumerate(nums):
            forward.append( forward[-1] * num )
            backward.append( backward[-1] * nums[~index])

        result = []

        for index in range(len(nums)):
            
            forward_mul = forward[ index ] 
            backward_mul = backward[ len(forward) - (index + 2) ]
            result.append( forward_mul * backward_mul )

        return result
