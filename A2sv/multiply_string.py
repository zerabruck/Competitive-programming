class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        dicto={}
        for i in range(10):
            dicto[f'{i}']=i

        first_num=0
        for i in range(len(num1)):
            n=1
            for j in range(i+1,len(num1)):
                n*=10
            first_num+=dicto[num1[i]] * n
        
        second_num=0
        for i in range(len(num2)):
            n=1
            for j in range(i+1,len(num2)):
                n*=10
            second_num+=dicto[num2[i]] * n


        return f'{first_num*second_num}'