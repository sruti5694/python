student = {'harry':75,'rohan':85,'nimish':65,'laksh':95,'shubham':55,'priya':45,'riya':95}
print(student)
# adding new key-value pairs in dictionary
student['me_hu_don'] = 90
student['don_ko_pakdna'] = 100
student['mushkil_nahi_namunkin_hai'] = 110
print(student)
# update key-value pairs in dictionary
student['harry'] = 99
print(student)
# accessing single key-value pair from the dictionary
print(student['rohan'])
print(student.get('nimish'))
# accessing all keys from the dictionary
print(student.keys())
# accessing all values from the dictionary
print(student.values())
# accessing all key-value pairs from the dictionary
print(student.items())
del student['priya']
print(student)
