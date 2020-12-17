# Positional arument (order matters)
def add(x, y):
    c = x + y
    print(c)


# Keyword arguements (order dosen't matters)
def show(name, age):
    print(name, age)


# default argument
def show1(name='hello', age='89'):
    print(name, age)

#Variable length argument
def fun(*num):
    sum = 0
    for i in range(len(num)):
        sum = sum + num[i]
    print(sum)

# keyword variable length arguments
def add1(**num):
    z = num['a']+num['b']
    print('sum1 = ',z)

# MAIN
add(2, 5)

# show(age = 18 , name= 'raja')
show(age=int(input('Enter age: ')), name=input('name : '))  # choose either of 3 cases
# show(age = 18, name= input())

show1(age=18)
# show1(age=input("age: "),name=input("Enter name: "))       #choose either of 2 cases

fun(10,25)
fun(10,55,58,79)

add1(a = 5,b = 6)