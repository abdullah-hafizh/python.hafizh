student = 'Alhazen'

try:
    print(student)
except NameError:
    print('variabel tidak ditemukan')
except:
    print('ada erorr')
else:
    print('run succesfully')
finally:
    print('script has run')
    
for i in range(10):
    print(i)

print('i comfused with python')
print(30*'=')

loop = int(input('enter a number: '))

if loop <= 1:
    raise Exception('number must be  > 1')
else:
    for i in range(loop):
        print('i comfused with python')