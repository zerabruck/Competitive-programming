height = [0,2]

biggest=0
for i in range(len(height)):
    for j in range(i,len(height)):
        if(height[i]<=height[j] and height[i] * (j-i) > biggest ):   
            biggest=height[i] * (j-i)
        elif(height[i]>height[j] and height[j] * (j-i) > biggest ):   
            biggest=height[j] * (j-i)

            
    

print(biggest)
