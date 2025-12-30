names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy']
# first i tell -> what to store in newlist 
new_list = [i for i in names if(len(i))>=5]
print(new_list)
new_list = [i for i in names if(i.endswith('e'))]
print(new_list)
new_list1 = [i for i in names if any(j in i.lower() for j in 'aeiou')]
print(new_list1)