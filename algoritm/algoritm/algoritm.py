import sys
import math
import recursion
import binary_search
import selection_sort
                                               
not_sorted_list=[2,-10,4,1,9,-14,4,9,0,-1]          # not sorted list for selection_sort

i=10                                                # variable for recursion.recursion(i)
x=10

mass=[1,2,3,4]                                      # Sum for recursion
sum=0
len=len(mass)
z=0


def main():
    #res=binary_search.binary_search()
    #print ("Item are in "+str(res)+" element of mass")

    #mew_arr=selection_sort.selection_sort(not_sorted_list)
    #print ("Sort mass:"+str(mew_arr))

    #recursion.recursion(i)
    #res=recursion.fact(x)
    #print (res)

    #res=recursion.recursion_mass (mass,sum)
    #print (res) 

    res=recursion.recursion_mass_2(mass,len)
    print (res)


    











if __name__ == '__main__':
    main()

