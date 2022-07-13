def my_print(b):
    if (len(b)==0): print("No One")
    elif (len(b)==1): print(b[0])
    elif (len(b)==2): print(set(b[0]).intersection(b[1]))
    else:print(set(set(b[0]).intersection(set(b[1]))).intersection(set(b[2])))
def my_function(lst1):
    a={}
    array=[]
    for x in lst1:
        a[x]=a.get(x,0)+1
    l=sorted(a.values())
    if l[len(l)-1]>1:
       print("we have That they have at least one recurring organ")
       print(lst1)
       return True
    else:return False
lst1 = [11,  7, 5,  8, 5,  37,  11, 5]
lst2 = [22, 8,10, 1, 11]
lst3 = [ 71, 3,11,11, 22, 8, 2, 14, 1]
b=[]
if (my_function(lst1)): b.append(lst1)
if (my_function(lst2)): b.append(lst2)
if (my_function(lst3)): b.append(lst3)
print("the result is :")
my_print(b)
