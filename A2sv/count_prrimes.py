class Solution:
    def countPrimes(self, n: int) -> int:
        eles = [ i for i in range(1, n + 1)]
        count = 0
        for ele in range(1, len(eles) - 1):
            if eles[ele] != 0:
                count += 1
                mult = eles[ele]
                multipls = eles[ele]
                while mult * multipls - 1 < n:
                    eles[mult * multipls - 1] = 0
                    multipls += 1
        return count
