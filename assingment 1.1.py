b = []
a = ['asd', 'asdw', 'qqq', 'eww']
l = len(a)
n = int(input("Enter the number : "))
for i in range(l):
    if (n >= len(a[i])):
        b.append(a[i])
print(b, 'N=', n)
