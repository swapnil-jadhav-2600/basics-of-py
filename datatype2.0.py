x = {1:"a"}
print(x)
x[2] = 'b'
print(x)


x = {1:'a', 2:['e','f','g']}
print(x)
print(x.keys())
print(x[2])
print(x[2][2])
x.pop(1)
x.clear()
print(x)

