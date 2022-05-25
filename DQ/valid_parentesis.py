class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        reference={"(":")","[":"]",'{':'}'}

        for i in s:
            if(i in reference.keys()):
                stack.append(i)
            elif(len(stack)==0):
                return False

            else:
                value=stack.pop(-1)
                if(reference[value]==i):
                    
                    continue
                else:

                    return False
                    break
        if(len(stack)==0):
            return True
        else:
            return False

        