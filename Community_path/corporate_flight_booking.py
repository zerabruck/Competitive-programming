class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        
        
        dict={}
        for i in range(1,n+1):
            dict[i]=0
        for i in bookings:
            dict[i[0]]+=i[2]
            if(i[1]+1 in dict ):
                    dict[i[1]+1]-=i[2]



        values=list(dict.values())
        for j in range(1,len(values)):  
            values[j]=values[j] +values[j-1]

        
        return values
        