class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        """
        first i will make the zeros in nums one go to the top while not losing the 
        relative order of the non zero elements in nums

        then i will have a pointer that starts at the non-zero element on nums1 and i will use
        two pointer to find an element the element that is less than the other and
        i will insert the smaller element in the nums then i will add the pointer value 
        by one and the pointer to the next insertion point by one
        """

        holder = len(nums1) - 1

        for seeker in range(len(nums1) - 1, -1, -1):
            if nums1[seeker] != 0:
                nums1[seeker] , nums1[holder] = nums1[holder] , nums1[seeker]
                holder -= 1

        holder += 1
        second_pointer = 0
        entery_pointer = 0

        while(holder < len(nums1) and second_pointer < len(nums2)):
            if nums1[holder] <= nums2[second_pointer]:
                nums1[entery_pointer] = nums1[holder]
                holder += 1

            else:
                nums1[entery_pointer] = nums2[second_pointer]
                second_pointer += 1

        nums

         
        