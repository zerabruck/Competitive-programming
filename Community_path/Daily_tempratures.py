class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperatures.reverse()
        decreasing_stack=[]
        answers=[]

        for i in range(len(temperatures)):
            while(True):
                if(len(decreasing_stack)==0):
                    decreasing_stack.append(i)
                    break
                elif(temperatures[i]>=temperatures[decreasing_stack[-1]]):
                    decreasing_stack.pop(-1)
                elif(temperatures[i]<temperatures[decreasing_stack[-1]]):
                    decreasing_stack.append(i)
                    break
            if(len(decreasing_stack)==1):
                answers.append(0)
            else:

                answers.append(decreasing_stack[-1]-decreasing_stack[-2])

        answers.reverse()
        return answers
