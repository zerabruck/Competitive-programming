class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if len(stack) == 0:
                stack.append((char, 1))

            elif stack[-1][0] == char:
                stack[-1] = (stack[-1][0], stack[-1][1] + 1)

            else:
                stack.append((char, 1))

            if stack[-1][1] == k:
                stack.pop()

        result = ''
        for ele in stack:
            result += ele[0] * ele[1]
        return result
