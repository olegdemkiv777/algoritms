import sys
import math

my_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]    # Sorted list
not_sorted_list=[2,-10,4,1,9,-14,4,9,0,-1]          # not sorted list
item=1                                              # Search number

def binary_search(list, item):
    print ("All list "+str(list))

    low=0
    high=len(list)-1    # -1 becouse element list start counter from 0.    
    i=0

    while low<=high:
        i=i+1
        mid=int((low+high)/2)
        guess=list[mid]
        if guess==item:    
            print ("How many steps algorithm did "+str(i))
            return mid 
        if guess>item:
            high=mid-1
        else:
            low=mid+1
    return None
#########################################################################


def find_smallest(not_sorted_list):
    #print ("Input massive: "+str(not_sorted_list))
    smallest=not_sorted_list[0]
    smallest_index=0
    #for i in range(1, len(not_sorted_list)):   # Why 1 in range
    for i in range(len(not_sorted_list)):
        if not_sorted_list[i]<smallest:
            smallest=not_sorted_list[i]
            smallest_index=i
    return smallest_index

def selection_sort(not_sorted_list):
    new_arr=[]
    for i in range(1, len(not_sorted_list)):
        smallest=find_smallest(not_sorted_list)
        new_arr.append(not_sorted_list.pop(smallest))
    return new_arr










def main():
    res=binary_search(my_list, item)
    print (res)

    mew_arr=selection_sort(not_sorted_list)
    print ("Sort mass:"+str(mew_arr))




























if __name__ == '__main__':
    main()

