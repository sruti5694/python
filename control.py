#there are three control statement that can be used with for and while loop to alter their behavior.i
#they are pass, continue, and break 
'''
k = 1
while(k<5):
    pass

for j in range(1,5):
    pass
'''
for i in range(1,5):
    if(i%2==0):
        continue
    print(i,end=" ")
print("\n")
for i in range(1,5):
    if(i%2==0):
        break
    print(i,end=" ")
