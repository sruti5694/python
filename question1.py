# def arr_add():
#     arr = []
#     n = int(input("enter size of array: "))
#     for _ in range(n):
#         i = int(input())
#         arr.append(i)
#     print(arr,end=" ")
#     repeat = []
#     for i in range(arr[len(arr)-1]):
#         if i not in arr:
#             repeat.append(i)
#     print(repeat,end=" ")
# arr_add()

# def string_char():
#     str1 = input("enter the string: ")
#     left = 0
#     result = 0
#     seen = set()
#     for right in range(len(str1)):
#         while str1[right] in seen:
#             seen.remove(str1[left])
#             left += 1
#         seen.add(str1[right])
#         result = max(result,right - left + 1)
#     print(result)
# string_char()
def  first_occurance():
    pass
    str1 = input("enter the string:")
    char = []
    for i in range(len(str1)):
        if str1[i] not in char and str1.count(str1[i])==1:
            char.append(str1[i])
    print(char[0] if char else -1) # if char is not empty print first element else print -1
first_occurance()

# Input:
# "abcabcbb"
# Output:
# 3 (The answer is "abc")

# Input:
# "bbbbb"
# Output:
# 1 (The answer is "b")

# Input:
# "pwwkew"
# Output:
# 3 (The answer is "wke")