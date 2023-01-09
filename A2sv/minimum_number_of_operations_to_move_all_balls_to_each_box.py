class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        one_ball = []
        moves_taken = []

        for i in range(len(boxes)):
            if boxes[i] == '1':
                one_ball.append(i)
    
        for i in range(len(boxes)):
            total_moves = 0
            for j in one_ball:
                total_moves += abs(i - j)

            moves_taken.append(total_moves)

        return moves_taken


        

