# def Addition(a,b):
#     print(f"Addition of two numbers are...{a} + {b} = {a+b}")
# a = int(input("enter the first number... "))
# b = int(input("enter the second number... "))
# Addition(a,b)

# def array1():
#     arr = []
#     n = int(input("enter the size array... "))
#     for _ in range(n):
#         i = int(input("enter"))
#         arr.append(i)
#     print(arr,end=" ")
#     for i in arr:
#         print(i,end="")
# array1()

# def array2():
#     arr = []
#     n = int(input("enter the size array... "))
#     for _ in range(n):
#         i = int(input("enter"))
#         arr.append(i)
#     for i in range(len(arr)):
#         print(arr[i],end=" ")
# array2()


# def array3():
#     arr = []
#     n = int(input("enter the size array... "))
#     for _ in range(n):
#         i = int(input("enter"))
#         arr.append(i)
#     for i in range(arr[0],arr[-1]):
#         print(i,end=" ")
# array3()


# def array4():
#     arr = []
#     n = int(input("enter the size array... "))
#     for _ in range(n):
#         i = int(input("enter"))
#         arr.append(i)
#     for i in range(arr[len(arr)-1]):
#         print(i)
# array4()

# def missing_num():
#     arr = []
#     n = int(input("enter the size array... "))
#     for _ in range(n):
#         i = int(input("enter"))
#         arr.append(i)
#     missing = []
#     for i in range(arr[0],arr[-1]):
#         if i not in arr:
#             missing.append(i)
#     print(missing,end=" ")
# missing_num()

# 1.
# name = 'shruti'
# new_name = list(name)
# new_name.reverse()
# print("".join(new_name))

# 2
# print(name[::-1]) #start : stop: step -1=>move backword
# print(name[::1])
# 3
# print("".join(reversed(name)))

# def addeight():
#     arr = []
#     n = int(input("enter the size of array=>"))
#     for _ in range(n):
#         i = int(input())
#         arr.append(i)
#     print(i,end=" ")
#     eight = []
#     for i in range(len(arr)-1):
#         if(arr[i] + arr[i+1]==8):
#             eight.append((arr[i],arr[i+1]))
#         elif(arr[i]==8):
#             eight.append((arr[i],)) # tuple without coma its only a number
#     print(eight,end=" ")
# addeight()

# def repeatnum():
#     arr = []
#     n = int(input("enter the size of array=>"))
#     for _ in range(n):
#         i = int(input())
#         arr.append(i)
#     print(i,end=" ")
#     repeat = []
#     for i in range(len(arr)):
#         if arr.count(arr[i])>1 and (arr[i],arr.count(arr[i])) not in repeat:
#             repeat.append(((arr[i]),arr.count(arr[i])))
#     print(repeat,end=" ")
# repeatnum()
# i = 1
# while(i<=10):
#     print(f"{11}*{i} = {11*i}")
#     i +=1

# for i in range(5):
#     print(" "*i,"*"*(5-i))

# for i in range(5):
#     print(" "*(5-i),"*"*(i))


# for i in range(5):
#     print("*"*(5-i))
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# def repeat_num():
#     n = int(input("enter the size of array=> "))
#     arr = []
#     for _ in range(n):
#         i = int(input("enter the number"))
#         arr.append(i)
#     print(arr,end=" ")
#     repeat = []
#     for i in range(len(arr)):
#         if(arr.count(arr[i])>1 and (arr[i],arr.count(arr[i])) not in repeat):
#             repeat.append((arr[i],arr.count(arr[i])))
#     print(repeat,end=" ") 
# repeat_num()

# def unique_num():
#     n = int(input("enter the size of array=> "))
#     arr = []
#     for _ in range(n):
#         i = int(input("enter the number"))
#         arr.append(i)
#     unique = []
#     for i in range(len(arr)):
#         if arr.count(arr[i])<=1:
#             unique.append(arr[i])
#     print(unique,end=" ")
# unique_num()

# def repeat_num():
#     n = int(input("enter the size of array=> "))
#     arr = []
#     for _ in range(n):
#         i = int(input("enter the number"))
#         arr.append(i)
#     print(arr,end=" ")
#     repeat = []
#     for i in range(len(arr)):
#         if(arr.count(arr[i])>1 and (arr[i],arr.count(arr[i])) not in repeat):
#             repeat.append((arr[i],arr.count(arr[i])))
#     print(repeat,end=" ") 
# repeat_num()

# def missing_num():
#     n = int(input("enter the size of array=> "))
#     arr = []
#     for _ in range(n):
#         i = int(input("enter the number"))
#         arr.append(i)
#     print(arr,end=" ")
#     missing = []
#     for i in range(arr[len(arr)-1]):
#         if i not in arr:
#             missing.append(i)
#     print(missing,end=" ")
# missing_num() arr[len(arr)-1]