class Solution:
    def uncrossed_lines(self, index1, index2):
        if index1 >= len(self.nums1) or index2 >= len(self.nums2):
            return 0

        if (index1, index2) not in self.dp:
            not_choose = self.uncrossed_lines(index1 + 1, index2)
            choose = 0
            for ele in range(index2, len(self.nums2)):
                if self.nums1[index1] == self.nums2[ele]:
                    choose = 1 + self.uncrossed_lines(index1 + 1, ele + 1)
                    break
            self.dp[(index1, index2)] = max(choose, not_choose)
        return self.dp[(index1, index2)]
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        self.dp = {}
        self.nums1 = nums1
        self.nums2 = nums2
        return self.uncrossed_lines(0, 0)
        
