


from array import array
from pytz import country_names


nums =[1,2,3,1]

def is_duplicate(nums):
    arraying=nums.copy()
    for i in arraying:
        arraying.remove(i)
        for j in arraying:
             if (i==j):


                return True
         
     
    

    
            
    return False
print(is_duplicate(nums))