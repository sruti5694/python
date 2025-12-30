# def fibo(x):
#     a = 0
#     b = 1
#     for i in range(0,x+1):
#         c = a + b
#         a = b
#         b = c
#         print(c)
# x = int(input("enter the number... "))
# fibo(x)


   
def prime(x):
    pass
    for i in range(2,x+1):
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            print(i)
x = int(input("enter the number... "))
prime(x)