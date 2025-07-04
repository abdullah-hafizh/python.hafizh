try:
    number1 = int(input('enter number 1: '))
    number2 = int(input('enter number 2: '))

    div = number1 / number2
    print(f'{number1} / {number2} = {div}')
except ValueError:
    print('cannot input other than number')
except ZeroDivisionError:
    print('second number cannot zero')
except:
    print('ada erorr')