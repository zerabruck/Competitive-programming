nums = [1,5,233,7]

def winner(nums,score1,score2,turn):
    print(score1)
    print(score2)
    
    turn=1-turn
    if(len(nums)==0):
        if(score1>score2):
            return True
        else:
            return False
    
    elif(nums[0]>=nums[-1]):
        if(turn==1):
            score2+=nums[0]
        else:
            score1+=nums[0]
        nums.pop(0)
    elif(nums[0]<nums[-1]):
        if(turn==1):
            score2+=nums[-1]
        elif(turn==0):
            score1+=nums[-1]
        nums.pop(-1)
    
    return winner(nums,score1,score2,turn)

print(winner(nums,0,0,1))