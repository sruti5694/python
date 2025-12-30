# num = '1321'
# digit = '1'
# ans = []
# for i in range(len(num)):
#     if num[i]==digit:
#         num1 = num[:i]+num[(i+1):]
#         ans.append(num1)
# print(str(max(ans)))

# 2.

# n = int(input("enter the number... "))
# arr = [0]*(n+1)
# arr[0] = 0
# arr[1] = 1
# for i in range(1, n//2+1):
#     arr[2*i] = arr[i]
#     arr[2*i+1] = arr[i]+arr[i+1]
# print(arr)
# print(max(arr))
    
# 3.
# arr = [7, 8, 5, 5, 9, 2, 2, 0, 1, 6]
# max_value = 0
# n = len(arr)
# for start in range(n):
#     res = [arr[(start - i) % n] for i in range(n)]
#     ans = 0
#     total = 0
#     for j in res:
#         ans ^= j
#         total += ans
#     max_value = max(max_value,total)
# print(max_value)
# print(res)

# 4.
# n = int(input("enter the number... "))
# arr = []
# count =0
# for _ in range(n):
#     value = int(input())
#     arr.append(value)
#     arr.sort()
# for i in arr:
#     if len(arr)>1:
#         if i!=arr:
#             arr.remove(i)  
#         else:
#             arr.remove(i)
#         count +=1
            
# print("ans",count)

# 4.
n = int(input("enter the number... "))
arr = list(map(int,input().split()))
arr.sort()
count =0
while(len(arr)!=0):
    if arr[0]!=arr[-1]:
        arr.pop()
        arr.pop(0)
    else:
        arr.pop(0)
    count +=1
print("ans",count)

# 5.
# from itertools import combinations
# n = int(input())
# sub = []
# arr = list(map(int,input().split()))
# max_value = max(arr)
# ans = 0
# for i in range(1,len(arr)//2): 
#     comb = combinations(arr,i+1)
#     for i in comb:
#         sub.append(list(i))
# for a in sub:
#     for b in a:
#         ans = ans ^ b
#     if ans>max_value:
#         max_value = ans
# print(max_value)


# from itertools import combinations
# n = int(input())
# arr = list(map(int,input().split()))
# max_value = max(arr)
# ans = 0
# for i in range(1,len(arr)//2):
#     for comb in combinations(arr,i):
#         for a in comb:
#             ans ^= a
#         max_value = max(max_value,ans)
# print(max_value)



# x = int(input("x"))
# y = int(input("y"))
# ans =0
# n = int(input("enter the  size of array... "))
# arr = list(map(int,input().split()))
# for i in range(len(arr)):
#     arr[i] = arr[i]-1
# ans += x
# for i in range(len(arr)):
#     if(arr[i]!=0):
#         arr[i] = 0
#         ans = ans+y
# print(ans)
# def convertbase(m,minbase):
#     rem = m % minbase
#     m = m // minbase
#     while m >= minbase and (m % minbase == rem):
#        m = m // minbase
#     if m == rem:
#         return True
#     return False
# m = int(input())
# minbase = 2
# while not convertbase(m,minbase):
#     minbase = minbase + 1
# print(minbase)


#  dynamic programming 

# arr = [[2],[3,4],[6,5,7],[4,1,8,3]]
# n = len(arr)
# left =0
# right =0
# for i in range(n-2,-1,-1):
#     m = len(arr[i])
#     for j in range(m):
#         left = arr[i+1][j]
#         right = arr[i+1][j+1]
#         arr[i][j]+= min(left,right)
# print(arr[0][0])

# arr = [[101,100],[110,10],[1000,11]]
# arr1 = []
# for i in range(len(arr)):
#     value = sum(arr[i])
#     arr1.append(value)
# print(max(arr1))

# t = int(input())
# arr = []
# for i in range(t):
#     m, n = input().split()
#     M = int(m,2)
#     N = int(n,2)
#     sumof = M+N
#     arr.append(sumof)
# print(arr)
# print(max(arr))
# finall = bin(max(arr))
# print(bin(max(arr)))
# print(finall[2:])


# def sol():
#     name = input()
#     demo={}
#     for i in name:
#         if i not in demo:
#             demo[i] = name.count(i)
#     for i in range(len(name)):
#         if demo[name[i]] == 1:
#             return i+1
#     return -1
# print(sol())

# maxvalue = 0
# n = int(input())
# arr = list(map(int,input().split()))
# for start in range(len(arr)):
#     res = [arr[(start-i)%len(arr)]for i in range(len(arr))]
#     ans =0
#     total =0
#     for i in res:
#         ans ^= i
#         total +=ans
#         maxvalue = max(maxvalue,total)
#     print(maxvalue,end=" ")

# n = int(input())
# cards = list(input().split())
# i = int(input("enter starting index: "))
# targetcard = input("enter card: ")
# cnt = 0

# for j in range(i,len(cards)):
#     if(cards[j]==targetcard):
#         break
#     cnt +=1
# print(cnt)


# n = int(input())
# cards = list(input().split())
# i = int(input("enter starting index: "))
# targetcard = input("enter card: ")


