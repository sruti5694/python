names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy']
names[5]='mark'
print(names)
names[2:4]=['kitty','cartoon']
print(names)
# list shrink because 1:8 items are replace by toony and shark
names[1:9]=['toony','shark']
print(names)

#existing items are shifts toward right 
names[2:3] = ['pink','blue','orange','yellow','gray','maroon','white']
print(names)