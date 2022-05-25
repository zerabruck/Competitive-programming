class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators=['*','/','+','-']
        stack=[]

        for i in tokens:


            if(i not in operators):

                stack.append(int(i))
            else:
                if(i=='*'):
                    second=stack.pop(-1)
                    first=stack.pop(-1)
                    stack.append(first * second)
                elif(i=='/'):
                    second=stack.pop(-1)
                    first=stack.pop(-1)
                    value=first / second
                    if(value>0):
                        value=floor(value)
                    else:
                        value=ceil(value)


                    stack.append(value)
                elif(i=='+'):
                    second=stack.pop(-1)
                    first=stack.pop(-1)
                    stack.append(first + second)
                elif(i=='-'):
                    second=stack.pop(-1)
                    first=stack.pop(-1)
                    stack.append(first - second)
        return stack[0]

        