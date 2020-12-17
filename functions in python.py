# syntax  def fun_name():

# addition prog
def add():
    a = 10
    b = 25
    c = a+b
    print(c)
# arg passing(single and multiple)
def mul(x , y):
    c = x*y
    return c

def eval(a,b,c):
    res = (a+b*c)
    return res

# even number prog
def even(l):
    for i in l:
        if(i%2 == 0):
            print(i)
    a = [ i for i in l if(i%2 == 0)]        # list compression method
    print(a)

# multiple return
def operation(a,b):
    return a+b,a-b,a*b,a//b

# nested fun
def disp():
    print("Welcome to the add fun prog")
    add()

# passing fun as a parameter
def fun(sh):
    print("Lets have fun learning together"+sh())
def show():
    return "Let the show begin"

# function returning another function
def display():
    def show():
        #return "Show method"
        print(("Display method"))
        return show
# main
print("Welcome")
add()
n = int(input("Enter number: "))
l = [i for i in range(n)]
even(l)

n1 = int(input("Enter x:"))
n2 = int(input("Enter y:"))
res = mul(n1,n2)
print(res)

n1 = int(input("Enter x:"))
n2 = int(input("Enter y:"))
n3 = int(input("Enter z:"))
res = eval(n1,n2,n3)
print(res)

n1 = int(input("Enter x:"))
n2 = int(input("Enter y:"))
print(operation(n1,n2))

print("Calling disp fun")
disp()

print("Calling fun function")
fun(show)

res = display()
print(res)
