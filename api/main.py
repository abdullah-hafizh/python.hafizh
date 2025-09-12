import json

data = {
    'employees' : [
        {
            'name' : 'Hafizh',
            'age' : 13   
        },
        {
            'name' : 'azzam',
            'age' : 15     
        },
        {
            'name' : 'miss salamah',
            'age' : 20     
        }        
    ],
    'student' : [
        {
            'name' : 'siapa aku?',
            'age' : 10     
        } 
    ]
}

print(type(data))

with open('api/data.json', 'w') as file:
    json.dump(data, file, indent=2)

print(json.dumps(data, indent=2))


text = """
{
    'country' : 'indonesia',
    'kabupaten' : 'penajam'
}
"""

print(text)
print(type(text))

#py_data = json.load(text)
#print(py_data)
#print(type(py_data))
#print(py_data['country'])