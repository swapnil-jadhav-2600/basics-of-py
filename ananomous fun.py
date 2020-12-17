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
