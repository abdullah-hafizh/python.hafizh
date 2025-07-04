addition = lambda num1, num2 : num1 + num2

num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))

add = addition(num1, num2)
print(f'{num1} + {num2} = {add}')


subs = lambda num1, num2 : num1 - num2

kurang = subs(num1, num2)
print(f'{num1} - {num2} = {kurang}')

kali = lambda num1, num2 : num1 * num2

multi = kali(num1, num2)
print(f'{num1} * {num2} = {multi}')


div = lambda num1, num2 : num1 / num2

bagi = div(num1, num2)
print(f'{num1} / {num2} = {bagi}')