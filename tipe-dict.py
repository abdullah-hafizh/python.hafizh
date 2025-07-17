student = {
    'name' :'ajis',
    'grade' : 10,
    'address' : 'jakarta',
    'beasiswa' : True,
    'prestasi' : ['juara 1 math', 'juara 2 sciense']
}

print(student)
print(type(student))

key_student = student.key()
print(key_student)

print(student['beasiswa'])
print(student['prestasi'])

for key in student: 
    print(key, ':', student[key])

student['address'] = 'tangerang'
print(student)

student['email'] = 'ahmad@student.mail'
print(student)

student.pop('beasiswa')
print(student)

student.popitem()
print(student)

student.clear()
print(student)

employee = dict(fullname='hafizh', address='kabupaten', salary=5000000, ismarried=False, skills=['game', 'math'])
