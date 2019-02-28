import sys
import math
import recursion
import binary_search
import selection_sort
                                               
not_sorted_list=[2,-10,4,1,9,-14,4,9,0,-1]          # not sorted list for selection_sort

def main():
    #res=binary_search.binary_search()
    #print ("Item are in "+str(res)+" element of mass")

    mew_arr=selection_sort.selection_sort(not_sorted_list)
    print ("Sort mass:"+str(mew_arr))

    #res=recursion.find_number()
    #print (res)


    











if __name__ == '__main__':
    main()

