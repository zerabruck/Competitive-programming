class Solution:
    def judgeCircle(self, moves: str) -> bool:
        direction = {
            "L":(0, -1),
            "R":(0, 1),
            "U":(1, 0),
            "D":(-1,0)
        }
        inital = (0,0)
        for dirr in moves:
            first = inital[0] + direction[dirr][0]
            second = inital[1] + direction[dirr][1]
            inital = (first, second)
        return inital == (0,0)

# L == 0, -1
# R == 0, +1
# U == +1, 0
# D == -1, 0
