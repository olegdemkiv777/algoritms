
def recursion (i):
    print (i)
    if i>0:
        recursion(i-1)
    else:
        print ("END")
        return 
   

def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)


def recursion_mass (mass, sum):
    for i in range(len(mass)):
        sum=sum+mass[i]
    return sum




def recursion_mass_2(mass,len):
    if len==1:
        return sum
    else:
        sum=sum+mass[i]
        i=i+i
        recursion_mass_2(mass, len-1)
        

    