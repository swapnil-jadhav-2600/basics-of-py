k = ['ten' ,'twenty' , 'thirty' ]
v = [10,20,30]
dict = {}
l1 = len(k)
l2 = len(v)
if(l1 == l2):
    for i in range(l1):
        dict[k[i]] = v[i]
print(dict)



# using zip fun

d = list(zip(k,v))
print(d)