name create file : x
try:
    file = open('file-handling/biodata.text', 'x')
except FileExistsError:
    print('file sudah ada')

# read file : r
try:
    file = open('file-handling/biodata.text', 'r')
    print(file.read())
except FileExistsError:
    print('File Not Found')

file = open('file-handling/note.text', 'w')
file.write('the most popular programming languange\n')
file.write('1. python\n')
file.write('2. javascript')

text = '''
3. Golang
4. Ruby
'''

file.write(text)
file.close()

# append file
file = open('file-handling/note.text', 'a')
file.write('5. java')
file.write('\n6. SQL')
file.close()

file = open('file-handling/todolist.text', 'a')
file.write('To Do List')
text = '''
1. study
2. shopping
'''

file.write(text)
file.close()

# project
file = open('file-handling/My Bio.txt')
file.write('About me\n')
file.write('Hello my')