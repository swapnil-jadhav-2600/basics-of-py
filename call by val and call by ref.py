# call by value
def val(x):
    x =15
    print(x,id(x))

def val1(lis):
    lis.append(6)
    #print(lis,id(lis))

def change(str1):
    str1 += "how are you?"
    print("printing the string outside", str1)

def fib(n):
    if(n <= 1):
        return n
    else:
        return(fib(n-1) + fib(n-2))
#MAIN

x = 10
val(x)
print(x,id(x))

lis = [1,2,3,4,5]
print(lis,id(lis))
val1(lis)
print(lis,id(lis))

str1 = "hi hellow namaste!"
change(str1)
print("printing the string outside",str1)

n = int(input("Enter no : "))
if(n<=0):
    print('invalid')
else:
    print("Fibo series :")
    #z = [i for i in range(n) print(fib(i))]
    for i in range(n):
        print(fib(i))