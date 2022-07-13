globmale = {}
globfemale = {}
def print_values_above(data_set:set,x:(float,int)=0.01):
    if not isinstance(x,(int,float)): raise TypeError("the params is not int or float")
    elif x<=0: raise  TypeError("The number must  be Positive")
    elif (x==0.01):
        print("Now print all the organs of the dictionary")
        print(data_set.items())
    elif x>0:
        c=0
        for k,v in data_set.items():
            if (v["age"]>x):
                if c==0:
                    print("Ages greater than the number received")
                print(k,v)
                c=1
        if (c==0): print("There is no age greater than the number received")
def find_median_average(data_set:set):
    a=[]
    sum=0
    for v in data_set.values():
        a.append(v["age"])
        sum+=v["age"]
    a = sorted(a)
    print("sort Age is :",a)
    print("mean:",sum/len(a))
    if (len(a)%2==1):
        print("median :",a[len(a)//2])
    else :
        y=(a[len(a)//2]+a[len(a)//2-1])/2
        print("median :",y)
def split_male_female(data_set):
    global globmale
    global globfemale
    for k, v in data_set.items():
        if v["sex"] == "male":
            globmale[k] = v
        else:
            globfemale[k] = v
data_set = {123: {"name": "Tal", "sex": "male", "age": 22},
            234: {"sex": "female", "age": 57, "ID": 17686401, "name": "Anat"},
            176864301: {"sex": "female", "age": 25, "height": 1.65, "name": "areej"},
            12345: {"sex": "male", "age": 30, "height": 1.7, "name": "waseem"}}
split_male_female(data_set)
print("set male is:",globmale)
print("set female is:",globfemale)
find_median_average(data_set)
print_values_above(data_set,25)