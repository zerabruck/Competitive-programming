class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = set( ["/" , "+" , "*" , "-"])
        stack = []
        for token in tokens:
            if token not in signs:
                stack.append(int(token))

            elif token == '+' :
                second = stack.pop()
                first = stack.pop()
                val = first + second
                stack.append(val)
            elif token == '-' :
                second = stack.pop()
                first = stack.pop()
                val = first - second
                stack.append(val)
            elif token == '*' :
                second = stack.pop()
                first = stack.pop()
                val = first * second
                stack.append(val)
            elif token == '/' :
                second = stack.pop()
                first = stack.pop()
                val = first / second
                stack.append(int(val))

        return stack[-1]
