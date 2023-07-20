class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        sum_num = 0
        last = 0
        for roman in s:
            if last != 0 and last < romans[roman]:
                sum_num -= last
                sum_num += (romans[roman] - last)
            else:
                sum_num += romans[roman]
            last = romans[roman]
        return sum_num
