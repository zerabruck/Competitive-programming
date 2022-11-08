class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if(k==len(num)):
            return '0'
        
        i_stack=[]
        
        for i in range(len(num)):
            if(len(i_stack)==0):
                i_stack.append(num[i])
                
            elif(int(num[i])<int(i_stack[-1])):
                while(True):
                    if(len(i_stack)==0 ):
                        i_stack.append(num[i])
                        break
                                              
                    if(int(i_stack[-1])>int(num[i])):
                        i_stack.pop()
                        k-=1
                        
                        
                    else:
                        i_stack.append(num[i])
                        break
                        
                    if(k==0):
                        value="".join(i_stack) + num[i:]
                        for i in range(len(value)):
                            if(value[i]!="0"):
                                return value[i:]
                            if(i==len(value)-1):
                                return '0'             
                        
            else:
                i_stack.append(num[i])
                
        
        value="".join(i_stack[:-k])
        
        for i in range(len(value)):
            if(value[i]!="0"):
                return value[i:]
            if(i==len(value)-1):
                return '0'       
                
         

                        
            
                
                    

                



                
                
                
                

        