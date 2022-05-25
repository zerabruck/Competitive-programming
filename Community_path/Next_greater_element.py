class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.reverse()
        array=[]
        for i in nums1:
            value=-1
            for j in nums2:
                if(i<j):
                    value=j
                elif(i==j):
                    array.append(value)
                    break
        return array

