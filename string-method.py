#string concating
str1 = 'caption'
str2 = 'america'
print(str1+" "+str2)
#string formating
name = 'harry'
age = 21
designation='web-developer'
statement = "my name is {} and I am a {} Currently working as {}"
print(statement.format(name,age,designation))
print(f"my name is {name} and I am a {age} Currently working as {designation}")
x = '12'
y = '10'
print(int(x)+int(y))

#index place argument
quantity = 2
fruits = 'apples'
cost = 120.0
statement = "i want to buy {0} {1}Kgs which cost {2} dolars"
print(statement.format(fruits,quantity,cost))