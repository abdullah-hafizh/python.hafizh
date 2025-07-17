n = 1

while n < 11: 
  print('I like python')
  n += 1

names = ['Salamah', 'Azzam', 'Hafizh']

for name in names: 
  print('Hello ' + name)

for i in range(2,11,2):
  print(i)
else:
  print('Loop finished')
  

for i in range(10):
  print(i)
  if i == 5:
    break

number = 0
while number < 10:
  number += 1
  if number == 5:
    continue
  print(number) 
else:
  print('Loop finished without break')

# while 10 < 20:
#   pass

fruits = ['apple', 'banana', 'manggo',]
colors = ['black', 'purple', 'blue',]

for fruit in fruits:
  for color in colors:
    print(f'{fruit} with color {color}')



# PROJECT
number = int(input('how many Loop: '))
choice = input('even or odd: ').lower()

if choice == 'even':
  for i in range(number):
    if i % 2 == 1:
      print(i)
elif choice == 'odd':
  for i in range(number):
    if i % 2 == 1:
      print(i)
else:
  print('invalid input')