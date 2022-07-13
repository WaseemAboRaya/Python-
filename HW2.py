def my_function(n,a):
    while(n>0):
        a[n%10]=a.get(n%10,0)+1
        n=n//10
    return a
lst = [31, 99, 3, 1943,82]
a={}
for n in lst:
    a=(my_function(n,a))
print(sorted(a.keys()))
print(((sorted(a.keys())))[::-1])




