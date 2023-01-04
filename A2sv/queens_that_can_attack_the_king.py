class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        result = []
        set_queens = { (i,j) for i,j in queens}
        

        for i in [1,0,-1]:
            for j in [1,0,-1]:
                for k in range(0,8):
                    first,second = king[0] + i*k, king[1] + j*k
                    if (first,second) in set_queens:
                        result.append([first,second])
                        break
        
        return result