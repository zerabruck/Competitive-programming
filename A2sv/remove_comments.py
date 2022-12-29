class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result=[]
        string=''
        flag=False
        for i in range(len(source)):
            line=source[i]
            char=0

            while(char<len(line)):
               
                if flag:
                    if line[char:char+2]=='*/' :
                        flag=False
                        char+=2
                        if char>=len(line):
                            if len(string)!=0 and char>=len(line):
                                result.append(string)
                                string=''
                        continue

                    char+=1
                elif line[char:char+2]=='/*':
                    flag=True
                    char+=2
                    continue


                elif(line[char:char+2]=='//'):
                    if len(string)!=0:
                        result.append(string)
                        string=''
                    break

                else:
                    string+=line[char]
                    if(char==len(line)-1):
                        # string+=line[char+1]
                        if len(string)!=0:
                            result.append(string)
                            string=''

                    char+=1

        return result

                        