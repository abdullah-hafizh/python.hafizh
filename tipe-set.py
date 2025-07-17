numbers = {0,1,9,2,8,3,7,4,6,5}
print(numbers)
print(type(numbers))

fruits = {'apple', 'banana', 'manggo', 'banana'}
print(fruits)
print(type(fruits))

# print(fruits[1]) # error
 for fruit in fruits:
    print(fruits)

# add
fruits.add('watermelon')
print(fruits)

# discard
fruits.discard('apple')
print(fruits)

fruits.discard('pir')
print(fruits)

# remove
fruits.remove('banana')
print(fruits)

# fruits.remove('pir') #error
# print(fruits)

# pop - remove random item
fruits.pop()
print(fruits)

animals = {'cat', 'dog', 'fish', 'bird', 'panda'}
amphibians = set(('frog', 'salamander'))

print(animals)
print(amphibians)

animals.update(amphibians)
print(animals)

mamalia = ['dolphin', 'whale']
animals.update(mamalia)
print(animals)