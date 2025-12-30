# colors = ['red','green','blue','purple','yellow','orange','brown']
# colors.insert(5,'black')
# print(colors)
# colors.append('pink')
# print(colors)
# citys = ['New York','Los Angeles','Chicago','Houston','Phoenix']
# colors.extend(citys)
# print(colors)
# colors[2] = 'white'
# print(colors)
# # colors[1:7]=['gray','cyan']
# print(colors)
# colors[1:3]=['gray','cyan','magenta','lime','teal','navy','maroon']
# print(colors)
# colors.sort(reverse=True)
# print(colors)
# colors.sort()
# print(colors)
# print(colors.count('navy'))
# print(colors.index('orange'))
# print(len(colors))
# colors.remove('pink')
# print(colors)
# colors.pop(4)
# print(colors)
# del colors[7]
# print(colors)

# colors = ('red','green','blue','purple','yellow','orange','brown')
# print(colors)
# print(colors[3])
# new_colors = list(colors)
# new_colors.append('pink')
# colors = tuple(new_colors)
# print(colors)
# new_colors = list(colors)
# new_colors[2] = 'white'
# citys = ('New York','Los Angeles','Chicago','Houston','Phoenix')
# new_citys = list(citys)
# new_colors.extend(new_citys)
# print(new_colors)

# colors = tuple(new_colors)
# print(colors)
# (ray, harry,lokesh,riyan,vihan )= citys
# print(harry)
# print(lokesh)
# print(riyan)
# print(vihan)
# print(ray)
# info = {'name':'harray','age':21,'city':'new york','profession':'developer'}
# print(info)
# info['age']=22
# print(info)
# info.update({'food':'burger','color':'blue'})
# print(info)
# print(info.keys())
# print(info.values())
# print(info.items())
# print(info['name'])
# print(info.get('name'))
# info.pop('city')
# print(info)
# info.popitem()
# print(info)
# del info['profession']
# print(info)

# new_info = info.copy()
# print(new_info)
# new1 = dict(info)
# print(new1)
# new_info = {'harry',21,'new york','developer','lokesh',22,'los angeles','designer'}
# print(new_info)
# new_info.add('vihan')
# new_info.update({'graphic designer',23,'chicago'})
# new_info.remove('developer')
# new_info.pop()
# new_info.discard('developer')
# print(type(new_info))
# print(len(new_info))
# print(new_info)

# print(set())
# print(type({}))
# print(type([]))
# print(type(()))
# new_info = {'harry',21,'Madrid','new york','Tokyo','developer','lokesh',22,'los angeles','designer'}
# citys = {"Tokyo", "Madrid"}
# n1 = new_info.union(citys)
# print(n1)
# n2 = new_info.intersection(citys)
# print(n2)
# n3 = new_info.difference(citys)
# print(n3)
# new_info.intersection_update(citys)
# print(new_info)
# n4 = new_info.symmetric_difference(citys)
# print(n4)
# n6 = citys.issubset(new_info)
# print(n6)
# n7 = new_info.issuperset(citys)
# print(n7)
# n8 = citys.isdisjoint(new_info)
# print(n8)
# colors = {'red','green','blue','purple','yellow','orange','brown'}
# n9 = citys.isdisjoint(colors)
# print(n9)
# fruits = {"apple", "banana"}
# new_items = ["cherry", "orange"]

# fruits.update(new_items)
# print(fruits)

# fruits = {"apple", "banana", "cherry", "date", "elderberry"}
# for i , value in enumerate(fruits,1):
#     print(i, value)
    
# def name_f(name,s_name):
#     print(f'Hello {name} {s_name} nice to meet you!')
# name = input("enter your name: ")
# s_name = input("enter your sarname: ")
# name_f(name,s_name)

# def name_f(s_name,name='harry',):
#     print(f'Hello {name} {s_name} nice to meet you!')
# s_name = input("enter your sarname: ")
# name_f(s_name)

# def name_f(*name):
#     print(f"hello {','.join(name)} nice to meet you!")
# name = {'harry','shubham','rohan','nimish','laksh','vihan'}
# name_f(*name)

# name = 'shruti'
# print(name[::-1])
# print("".join(reversed(name)))
# new_name = list(name)
# new_name.reverse()
# print(''.join(new_name))
# print(name[::1])

# def name_f(**name):
#     print(f'hello {','.join(map(str,name.values()))} nice to meet you!')
# name = {'shruti':21,'rohan':32,'harry':25,'laksh':54,'nimesh':23,'vihan':18}
# name_f(**name)

# def name_f(**info):
#     print(f'hello {','.join(map(str,info.values()))} nice to meet you...')
# info = {'name':'harry','designation':'software_developer','salary':50000,'location':'pune'}
# name_f(**info)

# def name_f(*info):
#     print(f'hello {','.join(map(str,info))} nice to meet you...')
# info = {'harry','software_developer',50000,'pune'}
# name_f(*info)

# def name_f(*info):
#     print(f'hello {','.join(map(str,info))} nice to meet you...')
# info = {'harry','software_developer',50000,'pune'}
# name_f(*info)

# for i in range(5):
#     print(i)
    
# for i in range(5,0,-1):
#     for j in range(1,i):
#         print(j,end=" ")
#     print()

# while(i<5):
#     print(i)
#     i+=1
i = 1

# while True:
#     if i%2==0:
#         print(i)
#         i+=1
#     else:
#         break

# while True:
#     if i >=5:
#         break
#     print(i)
#     i +=1
# i =2
# while True:
#     if i%2!=0:
#         break
#     print(i)
#     i+=1
    
# def arr_fun(b):
#     arr = []
#     for _ in range(n):
#         i = int(input())
#         arr.append(i)
#     print("the array is:",arr)
# n = int(input("enter the size of array... "))
# arr_fun(n)

# def arr_fun(n):
#     arr_set = set()
#     for _ in range(n):
#         i = int(input())
#         arr_set.add(i)
#     print("the array is:",arr_set)
# n = int(input("enter the size of array... "))
# arr_fun(n)

# def arr_fun(n):
#     arr_dict = {}
#     for _ in range(n):
#         i = int(input())
#         str_i = input("name: ")
#         arr_dict.update({i:str_i})
#     print("the array is:",arr_dict)
# n = int(input("enter the size of array... "))
# arr_fun(n)

# def arr_fun(n):
#     arr_dict = {}
#     for _ in range(n):
#         i = int(input())
#         str_i = input("name: ")
#         arr_dict[i] = str_i
#     print("the array is:",arr_dict)
# n = int(input("enter the size of array... "))
# arr_fun(n)

# def arr_fun(n):
#     arr_dict = {}
#     for _ in range(n):
#         i = int(input())
#         str_i = input("name: ")
#         arr_dict[i] = str_i
#     print("the array is:",arr_dict)
#     new_list = []
#     for i in list(arr_dict.keys()):
#         value = arr_dict.pop(i)
#         new_list.append(value)
#     print(new_list)
# n = int(input("enter the size of array... "))
# arr_fun(n)

# def arr_fun(n):
#     arr = []
#     for _ in range(n):
#         value = int(input())
#         arr.append(value)
#     print(arr)
#     sum = 0
#     for i in arr:
#         sum +=i
#     print(sum)
# n = int(input("enter size of array"))
# arr_fun(n)
        

# def arr_fun(n):
#     arr = []
#     for _ in range(n):
#         value = int(input())
#         arr.append(value)
#     print(arr)
#     print(sum(arr))
# n = int(input("enter size of array"))
# arr_fun(n)
        
# def fact_fun(n):
#     fact = []
#     for _ in range(n):
#         value = int(input())
#         fact.append(value)
#     print(fact)
#     fact1 = 1
#     for i in fact:
#         fact1 *= i
#     print(fact1)
# n = int(input())
# fact_fun(n)

# def reverse_fun(n):
#     rever = []
#     for _ in range(n):
#         value = int(input())
#         rever.append(value)
#     print(rever)
#     new = []
#     for i in rever:
#         num = i
#         rev = 0
#         while(num!=0):
#             digit = num%10
#             num = num //10
#             rev = rev *10+digit
#         new.append(rev)
#     print(new)
# n = int(int(input("enter the size of array")))
# reverse_fun(n)

# def max_arr(n):
#     arr_max = []
#     for _ in range(n):
#         value = int(input())
#         arr_max.append(value)
#     print(arr_max)
#     max_value = arr_max[0]
#     for i in arr_max:
#         if(max_value<i):
#             max_value = i
#     print(max_value)
# n = int(input())
# max_arr(n)

# def arr_average(n):
#     arr_avg = []
#     for _ in range(n):
#         value = int(input())
#         arr_avg.append(value)
#     print(arr_avg)
#     cal =0
#     for i in arr_avg:
#         cal += i
#     avg = cal/len(arr_avg)
#     print(avg)
# n = int(input())
# arr_average(n)

# def arr_even_number(n):
#     arr = []
#     for _ in range(n):
#         value = int(input())
#         arr.append(value)
#     print(arr)
#     arr_even = []
#     for i in arr:
#         if i%2==0:
#             arr_even.append(i)
#     print(arr_even)
# n = int(input())
# arr_even_number(n)

# def arr_fun(n):
#     arr = []
#     for _ in range(n):
#         value = int(input())
#         arr.append(value)
#     print(arr)
#     unique = []
#     for i in arr:
#         if i not in unique:
#             unique.append(i)
#     print(unique)
# n = int(input())
# arr_fun(n)

# def duplicates(n):
#     arr = []
#     for _ in range(n):
#         value = int(input())
#         arr.append(value)
#     print(arr)
#     dupli = []
#     for i in range(len(arr)):
#         if arr[i]not in dupli and arr.count(arr[i])>1:
#             dupli.append(arr[i])
#     print(dupli)
# n = int(input())
# duplicates(n)

# def duplicates(n):
#     arr = []
#     for _ in range(n):
#         value = int(input())
#         arr.append(value)
#     print(arr)
#     dupli = []
#     for i in arr:
#         if i not in[x[0] for x in dupli] and arr.count(i)>1:
#             dupli.append((i,arr.count(i)))
#     print(dupli)
# n = int(input())
# duplicates(n)


# def missing_num(n):
#     arr = []
#     for _ in range(n):
#         value = int(input())
#         arr.append(value)
#     print(arr)
#     missing = []
#     for i in range(arr[len(arr)-1]):
#         if i not in arr:
#             missing.append(i)
#     print(missing)
# n = int(input())
# missing_num(n)
 
# def eight_add(n):
#     arr = []
#     for _ in range(n):
#         value = int(input())
#         arr.append(value)
#     eight = []
#     for i in range(len(arr)-1):
#         if (arr[i]+arr[i+1]==8 and (arr[i],arr[i+1])not in eight):
#             eight.append((arr[i],arr[i+1]))
#     print(eight)
# n = int(input())
# eight_add(n)

# abcabcbb -> longest substring
def longest_sub(s):
    longest = ''
    for i in range(len(s)):
        arr = []
        for j in range(i,len(s)):
            if s[j] not in arr:
                arr.append(s[j])
            else:
                break
        if len(arr)>len(longest):
            longest = ''.join(arr)
    print("the longest substring is:",longest)
    print("the length of longest substring is:",len(longest))
s = input("enter the string:")
longest_sub(s)