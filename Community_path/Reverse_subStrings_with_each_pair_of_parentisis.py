class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        anoter_stack=[]
        for i in s:

            if(i==')'):
                while(True):
                    if(anoter_stack[-1]=="("):
                        anoter_stack.pop(-1)
                        break
                    value=anoter_stack.pop(-1)
                    stack.append(value)  
                     

                for i in stack:
                    anoter_stack.append(i)
                stack=[]
            else:
                anoter_stack.append(i)


        valueing=''
        for i in anoter_stack:
            valueing+=i
        return valueing
