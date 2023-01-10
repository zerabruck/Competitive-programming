from collections import defaultdict
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        characters = defaultdict(int)

        for i in board:
            for j in i:
                characters[j] +=1


        difference = characters['X'] - characters['O']

        if 0 <= difference < 2:
            count = 0
            
            for index,row in enumerate(board):
               
                sets = set(row)
                if  len(sets) == 1 and 'X' in sets:
                    count += 1
                    if characters['X'] - characters['O'] <= 0:

                        return False
                    for column in range(len(row)):
                        setting = set([ rowwing[column] for rowwing in board ])
                        if len(setting) == 1 and 'X' in setting:
                            count -= 1
                elif  len(sets) == 1 and 'O' in sets:
                    count += 1
                    
            for col in range(len(board[0])):
                setts = set([value[col] for value in board])
                if len(setts) == 1 and 'X' in setts:
                    if characters['X'] - characters['O'] <= 0:
                        return False
                    count+=1

                elif len(setts) == 1 and 'O' in setts:
                    if characters['X'] - characters['O'] > 0:
                        return False
                    count+=1
                
# -------------------------------------------

            if board[0][0] == board [1][1] == board[2][2] == "X":
                if characters['X'] - characters['O'] <= 0:
                        return False
                else:
                    count+=1
            if board[0][0] == board [1][1] == board[2][2] == "O":
                if characters['X'] - characters['O'] > 0:
                        return False
                count += 1
            if board[0][0] == board [1][1] == board[2][2] == "X" and   board[0][2] == board [1][1] == board[2][0] == "X" :
                count -= 1

            if board[0][2] == board [1][1] == board[2][0] == "X":
                if characters['X'] - characters['O'] <= 0:
                        return False
                else:
                    count+=1
            if board[0][2] == board [1][1] == board[2][0] == "O":
                if characters['X'] - characters['O'] > 0:
                        return False

                count += 1

            if count > 1:
                return False

            return True

        # print(characters)