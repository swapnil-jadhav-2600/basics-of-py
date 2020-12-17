# example 1 (Basic function  call)
def hello_dec(fun):
    def innner_hello_dec():
        print('Hello, this is before function execution!')
        fun()
        print('Hello, this is after fun is called')

    return innner_hello_dec

def fun_to_be_called():
    print('This is inside the function')

fun_to_be_called = hello_dec(fun_to_be_called)

fun_to_be_called()

# example 2 : 
def fun1(a,b):
    return a+b

res = 
