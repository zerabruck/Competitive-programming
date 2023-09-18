class Solution:
    def subseq(self, index1, index2):
        if index1 > index2:
            return 0
        if index1 >= len(self.s) or index2 < 0:
            return 0

        if index1 == index2 and self.s[index1] == self.s[index2]:
            return 1

        if (index1, index2) not in self.dp:
            if self.s[index1] == self.s[index2]:
                self.dp[(index1, index2)] = 2 + self.subseq(index1 + 1, index2 - 1)
            else:
                self.dp[(index1, index2)] = max(self.subseq(index1 + 1, index2), self.subseq(index1, index2 - 1))
        return self.dp[(index1, index2)]
    def longestPalindromeSubseq(self, s: str) -> int:
        self.dp = {}
        self.s = s
        return self.subseq(0, len(s) - 1)
        
