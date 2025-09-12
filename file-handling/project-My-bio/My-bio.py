file = open('file-handling/project-My-bio/My bio.txt', 'w')
file.write('about me\n')
file.write('My name is Hafizh\n')
file.write('i am 12 years old\n')

file.close()

file = open('file-handling/project-My-bio/My bio.txt', 'a')
file.write('My hobby is memorize Al-Quran and reading novel')

file.close()

try:
    file = open('file-handling/project-My-bio/My bio.txt', 'r')
    print(file.read())
except FileExistsError:
    print('File Not Found')