# lambda fun
y = lambda x,y : print(x+y,x*y)
print(y)
y(10,20)

y = lambda x,y : lambda z : print(x+y+z)
print(y)
y(10,20)

# returning a labda function
def add():
    y = 20
    return(lambda x : x+1)

a = add()
print(a(10))

#map, filter and reduce function
#  filter : returns filtered values from  a sequence 
lis = [1,2,3,4,5,6,7,8,9,10]
final_lis = list(filter ((lambda a : (a%2!=0)) , lis))
print(final_lis)

# map : 
#l1 = [1,2,3,4,5,6,7,8,9,10]
#fl = list( map(lambda x: (x+2) , 1)

# reduce 
from functools import reduce
li = [5,8,6,9,8]
sum = reduce((lambda b,c:b+c),li)
print(sum)

li = [1,2,3,4,5,6]
print('The maximum element in the list')
print(reduce(lambda a,b: (a if a>b else b) , li))

