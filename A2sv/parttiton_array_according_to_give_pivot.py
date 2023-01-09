class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_elements = []
        greater_elements = []
        equal_elements = []

        for num in nums:
            if num > pivot:
                greater_elements.append(num)

            elif num < pivot:
                less_elements.append(num)
            else:
                equal_elements.append(num)
        merged = less_elements + equal_elements + greater_elements
        return merged
