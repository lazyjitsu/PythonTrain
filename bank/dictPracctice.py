student = {'name': 'John', 'age': 22, 'courses': ['Math', 'Spanish']}

print(student.get('phone')) # will not print an error!

student['phone'] = '555-555-5555'


print(student.get('phone')) #prints None if key doesn't exist!

print(student)
student.update({'name':'Jane','age': 23, 'phone':'444-444-4444'})
print(student)

# set a default if key doesn't exist
print(student.get('MMA','Not Found'))

# a couple ways to delette
#del student['age']
# age = student.pop('age') save off the age in case u need it 
# len() of dict will return how many keys
print(len(student))
#lets see the keys
print(student.keys())
# to see values
print(student.values())
# to see both
print(student.items())
print(student)

# print keys again

for key in student:
    print(f"Key: {key}")

# print both key & value
for key,val in student.items():
    print(f"Key: {key} and val: {val}")