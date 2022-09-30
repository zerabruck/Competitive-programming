class Solution:
    def compress(self, chars: List[str]) -> int:
        
        newstring=''
        beg=0
        end=0
        count=0
        start=0
        while(True):
            if(end==len(chars) ):
                if(count!=1):
                    newstring=newstring+str(count)
                chars.clear()
                for i in newstring:
                    chars.append(i)

                return len(newstring) 
            elif(chars[beg]==chars[end]):
                if(start==0):
                    newstring=newstring+chars[beg]
                    count+=1
                    start=1
                else:
                    count+=1

                end+=1

            elif(chars[beg]!=chars[end] and start==1):
                if(count!=1):
                    newstring=newstring+str(count)

                count=0
                start=0
                beg=end