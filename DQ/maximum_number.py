piles =  [9,8,7,6,5,1,2,3,4]
piles.sort(reverse=True)
ranging=len(piles)//3
index=1
value=0
for i in range(ranging):
    value+=piles[index]
    index+=2


