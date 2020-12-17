x = [24,6.6,'hello']
print(x)
x.append('sup')
print(x)
x.insert(2,2600)
print(x)
x.remove(6.6)
print(x)


y = []
for z in range(10):
    y.append(z)
    print(y)
y.clear()
print(y)

a = []
for z in range(2):
    a.append(input("Enter name :"))
print(a)
print(a.pop(1))
print(a)

# more functions 1.remove 2.sort 3.index 4.copy

x = []
sum = 0
for i in range(1,51):
    x.append(i)
    if (i%2 == 0):
        sum = sum + i
print(sum)
print(x)

x = []
sum =0
while True:
    m = input("1.Enter number    2.Quit")
    if(m == 2):
        break
    else:
        n = int(input("Enter a number"))
        x.append(n)
        sum = sum + n
print(x)
print(sum)


