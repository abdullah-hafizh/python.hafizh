def addition(number1, number2):
    hasil = number1 + number2
    return hasil

def sub(number1, number2):
    hasil = number1 - number2
    return hasil

def multi(number1, number2):
    hasil = number1 * number2
    return hasil

def div(number1, number2):
    hasil = number1 / number2
    return hasil

number1 = int(input('enter first number: '))
number2 = int(input('enter second number: '))

add = addition(number1, number2)
print(f'{number1} + {number2} = {add}')

subs = addition(number1, number2)
print(f'{number1} - {number2} = {add}')

kali = addition(number1, number2)
print(f'{number1} * {number2} = {add}')

bagi = addition(number1, number2)
print(f'{number1} / {number2} = {add}')