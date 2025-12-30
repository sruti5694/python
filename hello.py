print('hello')

for i in range(5):
    print(i,end="")
    
x = 5
y = 10.5
z = 3+2j
print(type(x),type(y),type(z))

str = '1234'
print(int(str[0])+int(str[1]))
print(str[0]+str[1])

a = 5
print(float(a))
print(int(y))
print('none',bool(None))
print('emptylist',bool([]))

x = 13
if(x < 13):
    print("number is prime ")
else:
    print("number is not prime")