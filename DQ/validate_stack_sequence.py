class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]

        for i in popped:
            if(i in pushed):
                while(True):
                    if(pushed[0]==i):
                        pushed.remove(i)
                        break
                    else:
                        stack.append(pushed[0])
                        pushed.remove(pushed[0])
            elif(i ==stack[-1]):
                stack.pop(-1)
            else:
                return False
                
        return True