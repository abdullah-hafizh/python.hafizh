print('hello')

def myFunction():
    print('its no my function')

myFunction()
myFunction()
myFunction()
myFunction()
myFunction()

def sayHello(name, age):
    print(f'hello {name}, {age} years old')

sayHello('Abi', 37)
sayHello('Ummi', 36)
sayHello('Kaka', 18)
sayHello('Abang', 15)
sayHello('Salim', 10)
sayHello('Aisyah', 7)
sayHello('Atthallah', 3)
sayHello('Hanifah', 1)

def tambah(angka1, angka2):
    hasil = angka1 + angka2
    return hasil

y = tambah(1,9) * 10
print(y)

x = tambah(10,90)
print(x)

number1 = 60
number2 = 40
add = tambah(number1, number2)
print(f'{number1} + {number2} = {add}')