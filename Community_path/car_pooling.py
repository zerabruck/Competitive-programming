class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        

        dict={}


        for i in trips:
            if( i[2] not in dict):
                for j in range(0,i[2]+1):
                    if( j not in dict):
                        dict[j]=0

            dict[i[1]]+=i[0]

            if(i[2] in dict) :
                dict[i[2]]-=i[0]



        values=list(dict.values())

        for i in range(1,len(values)):
            values[i]=values[i] +values[i-1]


        truth=False
        if(max(values)<=capacity):
            truth=True
            
        return truth
