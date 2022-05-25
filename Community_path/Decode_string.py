class Solution:
    def decodeString(self, s: str) -> str:

        def decoder(s):
            first=0
            second=0
            for i in range(len(s)):

                if(s[i]=="["):
                    first=i
                elif(s[i]==']'):
                    second=i
                    break
                elif(i==len(s)-1):
                    return s

            ranging=first-3
            integer=''
            for i in range(3):
                try:
                    int(s[ranging])
                    integer+=s[ranging]
                except:
                    ranging+=1
                    integer=''
                    continue

                ranging+=1


            multiplied=int(integer) * s[first+1:second]
            s=s[:first-len(integer)] + multiplied +s[second+1:]

            return decoder(s)
        return decoder(s)

