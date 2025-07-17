def greeting(name):
    print(f'Hello {name}')

greeting('mis salamah')

greeting2 = lambda name : print(f'Hello {name}')

greeting2('hafizh')

def is_even(number):
    if number % 2 == 0:
        print('YES number is even')
    else:
        print('NO, the number is odd')

is_even(4)
is_even(5)

is_even2 = lambda number : print('YES') if number % 2 == 0 else print('NO')

is_even2(10)
is_even2(13)