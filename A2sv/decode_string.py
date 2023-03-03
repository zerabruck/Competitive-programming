class Solution:
    def decodeString(self, s: str) -> str:
        number = set(['0','1','2','3','4','5','6','7','8','9'])
        num = ""
        stack = []
        res = ''
        flag = False
        walker = -1
        for char in range(len(s)):
            if flag :
                if s[char] == "[" :
                    stack.append(s[char])

                elif s[char] == "]" :
                    stack.pop()
                
                if not len(stack) :
                    val = self.decodeString(s[ walker + 1 : char ])
                    num = int(num)
                    val = val * num
                    res += val
                    num = ''
                    flag = False

            elif s[char] in number :
                num += s[char]

            elif s[char] != "[" :
                res += s[char]

            else:
                stack.append('[')
                walker = char
                flag = True

        return res
