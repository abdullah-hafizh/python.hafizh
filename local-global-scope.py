x = 'global'
print(x, 'di luar fungsi')

def foo():
    y = 'local'
    print(x, 'di dalam fungsi')
    print(y, 'di dalam fungsi')

# print(y, 'di luar fungsi') # error y is not defined

foo()

score = 0
print('score awal : ', score)

def tambah_score():
    global score
    score += 10
    print('score bertambah', score)

tambah_score()
tambah_score()
tambah_score()
print('score saat ini', score)

text = 'global scope'

def myFunction():
    #print(text)
    text = 'local scope'
    print(text)

myFunction()
print(text)