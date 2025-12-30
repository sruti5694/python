def first_fun(name,l_name):
    print(f"hello {name} and my last_name is {l_name}...")
name = input("enter the first name: ")
l_name = input("enter the second name: ")
first_fun(name,l_name)

#Always put non-default arguments first, then default arguments.
#If you do it the opposite way, Python cannot figure out which value belongs to which parameter, and it assumes there are no more positional arguments → SyntaxError.
def first_fun1(l_name,name='shruti'):
    print(f"hey {name} what's your name {l_name}...")
l_name = input("enter the last name: ")
first_fun1(l_name)

#unpack posional argument
# unpack we store it into tuple
#if you pass first unpacking argument you have to lname as keyword argument
# Start with unpacking → store in tuple.
# Any argument after that → must be passed as keyword argument.

def first_fun2(lname,*names):
    print(lname,names)
names = ['harry','rohan','laksh','nimesh']
l_name = input("enter the last1 name: ")
first_fun2(*names,l_name)