from functools import reduce

def up_name(name):
    return name.upper()

names = ['john', 'mark', 'bob', 'alice']

names_upper = []
for name in names:
    names_upper.append(up_name(name))

print(names_upper)

print(32*'-')

names_upper2 = map(up_name, names)
print(list(names_upper2))



''''''''''''''''''''''''''''''''''''''''''''''''



def kuadrat(angka):
    return angka*angka

num = input('enter your number separate with space: ')

num_list = list(map(int, num.split()))
hasil_kuadrat = list(map(kuadrat, num_list))
print(hasil_kuadrat)



''''''''''''''''''''''''''''''''''''''''''''''''





# Filter
def even_nums(numbers):
    even_list = []

    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)

    print(even_list)

even_nums(range(1,101))

# filter
def is_even(n):
    return n % 2 == 0

even_numbers = filter(is_even, range(1,11))
print(list(even_numbers))

print(32*'-')
# reduce
def addition(number1, number2):
    return number1 + number2

hasil = reduce(addition, range(1,11))
print(hasil)
hasil = reduce(addition, range(1,101))
print(hasil)

