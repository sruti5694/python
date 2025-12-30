#conditional statement
#i take user input
'''
appleprize = int(input("enter the apple prize...\n"))
bugget = int(input("enter the bugget...\n"))
if(appleprize>=bugget):
    print("you will never get the apples...")
else:
    print("you will get apples...")
'''

#compare three numbers
'''
num1 = int(input("enter the first number..."))
num2 = int(input("enter the second number..."))
num3 = int(input("enter the third number..."))
if(num1==num2 and num1==num2):
    print("all are equal...")
elif(num1>=num2 and num1>=num3):
    print("num1 is greater number...",num1)
elif(num2>=num1 and num2>=num3):
    print("num2 is greater number",num2)
else:
    print(num3)
'''  
# to check number is +ve or -ve
Num = int(input("enter the first number..."))
if(Num<0):
    print("Number is -ve")
elif(Num>0):
    if(Num>=10 and Num<=20):
        print("number is between 10 to 20")
    elif(Num>=20 and Num<=30):
        print("number is between 20 to 30")
    elif(Num>=30 and Num<=40):
        print("number is between 30 to 40")
    else:
        print("number is greater than 40")
else:
    print("number is zero")
        
    
