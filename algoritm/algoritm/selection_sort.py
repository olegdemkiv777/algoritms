# page 57

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

