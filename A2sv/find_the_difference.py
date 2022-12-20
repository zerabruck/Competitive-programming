class Solution:
    def interpret(self, command: str) -> str:
        pointer=0
        result=''
        while(pointer<len(command)):
            if(command[pointer]!='('):
                result+='G'
                pointer+=1
            elif(command[pointer+1]!=')'):
                result+='al'
                pointer+=4
            else:
                result+='o'
                pointer+=2

        return result