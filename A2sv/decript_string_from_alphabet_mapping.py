class Solution:
    def freqAlphabets(self, s: str) -> str:
        dicto={}
        result=""
        order_a=97
        order_j=106
        for i in range(1,11):
            dicto[f"{i}"]=chr(order_a)
            order_a+=1

        for i in range(10,27):
            dicto[f"{i}#"]=chr(order_j)
            order_j+=1

        

        pointer=0
        # print(dicto)
        while(pointer<len(s)):
            if(pointer+2 <len(s) and s[pointer+2]=="#"):
                # print(dicto[s[pointer:pointer+3]])
                result+=dicto[s[pointer:pointer+3]]
                pointer+=3
            else:
                result+=dicto[s[pointer]]
                pointer+=1

        return result

            