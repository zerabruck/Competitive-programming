class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        end=int(sqrt(c))
        front = 0


        while(front <= end):
            c_val = end ** 2 + front ** 2
            if c_val > c:
                end -= 1
            elif c_val < c:
                front += 1

            else:
                return True

        return False