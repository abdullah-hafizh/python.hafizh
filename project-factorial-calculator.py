def factorial(number):
    if number == 1:
        return 1
    else:
        result = number * factorial(number-1)
        return result

number = int(input('enter your number: '))
hasil = factorial(number)
print(f'{number}! = {hasil}')

