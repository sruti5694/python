# for i in 'Abhishek':
#     print(i,end=" ")
# print("\n")
# print(len('Abhishek'))

# colors = ('red','blue','pink','green','yellow')
# for i in colors:
#     print(i)
# print("\n")

# for i in range(5):
#     print(i)
# print("\n")

# for i in range(5,10):
#     print(i)
# print("\n")

# for i in range(len(colors)):
#     print(colors[i])
# print("\n")

# numbers = [10,20,30,40,50]
# for i in range(len(numbers)):
#     print(numbers[i])
# print("\n")

# count = 5
# while(count > 0):
#     print(count)
#     count -= 1
# print("\n")

# count = 0
# while(count < len(numbers)):
#     print(numbers[count])
#     count +=  1
# print("\n")

# count = 0
# while(count < 5):
#     for i in range(5):
#         print("*",end=" ")
#         i += 1
#         print()
#         for j in range(i):
#             print("*",end=" ")
#     print("\n")
#     count += 1



# for i in range(5):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# print("\n")
# #  starting index , stoping index , step count
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# print("\n")

# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()
# print("\n")

# # for i in range(5, 0,-1):
# #     print(" " * i + "*" * (5-i+1)+ "*" * (5-i),end=" ")
# #     print()
# # print("\n")

# for i in range(5,0,-1):
#     print(" " * i + "*" * ((2*(5-i))+1),end=" ")
#     print()
# print("\n")

# for i in range(5,0,-1):
#     print(" " * (5-i) + "*" * ((2*(i))-1),end=" ")
#     print()
# print("\n")

# for i in range(5, 0, -1):
#     print(" " * i + "*" * (5 - i),end=" ")
#     print()
# for i in range(5, 0, -1):
#     print(" " * (5 - i) + "*" * i,end=" ")
#     print()
# print("\n")

# for i in range(5, 0,-1):
#     print("*"*(i),end=" ")
#     print()
# print("\n")
# for i in range(5):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# print("\n")
# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()
# print("\n")

# colors = ['pink', 'blue', 'orange', 'green', 'black']
# for i , value in enumerate(colors):
#     print(i,value)
# print()

# for i in range(1,4):
#     for j in range(1,4):
#         # print(i , "*" , j , "="  ,(i*j))
#         print(f"{i} * {j} = {i*j}")
#     print()

str1 = "Abhishek"
str2 = "".join(reversed(str1))
print(str2)