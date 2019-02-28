# page 23 

def binary_search(): 
    item=16                                              # Search numbe
    my_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]     # Sorted list
    print ("All list "+str(list))

    low=0
    high=len(my_list)-1                                  # -1 becouse element mass start counter from 0.    
    i=0

    while low<=high:
        i=i+1
        mid=int((low+high)/2)
        guess=my_list[mid]
        if guess==item:    
            print ("How many steps algorithm did "+str(i))
            return mid 
        if guess>item:
            high=mid-1
        else:
            low=mid+1
    return None

