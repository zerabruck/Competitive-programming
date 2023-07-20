class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [1]
        for i in range(n):
            value = stairs[i]
            if i - 1 >= 0:
                value += stairs[i - 1]
            stairs.append(value)
        return stairs[-1]
