import time

"""task 1"""
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        lst.append(a)
lst = []
n =10
fib(n)
lst_iter = iter(lst)

while True:
    time.sleep(1)
    try:
        print(next(lst_iter), end= ' ')

    except StopIteration:
        break


"""task 2"""
def checker(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def simple(n):
    current_number = 2
    while current_number <= n:
        if  checker(current_number):
            lst_1.append(current_number)

        current_number += 1

lst_1 = []
lst_iter_1 = iter(lst_1)
checker(9)
simple(6)

while True:
    time.sleep(1)
    try:
     print(next(lst_iter_1), end=' ')

    except StopIteration:
        break

"""task 3"""

def krutoe_chislo(chislo):
    divisors_sum = 1
    for i in range(2, int(chislo**0.5) + 1):
        if chislo % i == 0:
            divisors_sum += i
            if i != chislo // i:
                divisors_sum += chislo // i
    return divisors_sum == chislo

def vivodim_chsla(limit):
    for number in range(2, limit + 1):
        if krutoe_chislo(number):
            yield number


limit = 1000000000
for perfect_number in vivodim_chsla(limit):
    print(perfect_number)

"""task 6"""
generator_1 =[i // i for i in range(1,7)]
generator_3 = [sum(range(1, i + 1)) for i in range(1, 7)]
generator_2 = [i + 1 for i in range(6)]
generator_4 = [i *(i+1) * (i +2)// 6 for i in range(1, 6 + 1)]

print(generator_1)
print(generator_2)
print(generator_3)
print(generator_4)


"""task 7"""


def add_nomera(kontack, name, noviej_nomer):
    if name in kontack:
        kontack[name].append(noviej_nomer)
        print(f'nomer: {noviej_nomer} dobavlen k {name}')
    else:
        print(f'Contact {name} ne naiden')


def poisk_contacta(kontakt, nomer):
    poisk_nomera = {}
    for name, numbers in kontakt.items():
        if nomer in numbers:
            poisk_nomera[name] = numbers
    return print(poisk_nomera)


kontackti = {
    "Ben": ["89001234050", "+70504321009"],
    "Alice": ["210-220", "404-502", "894-005", "439-095"],
    "Nick": ["+16507811251"],
    "Alex": ["+4(908)273-22-42"],
    "Robert": ["51234047129", "92174043215"]}

Ben_nomer = int(input('enter nomer for Ben: '))
Alice_nomer = int(input('enter nomer for Alice: '))
Nick_nomer = int(input('enter nomer for Nick: '))
Alex_nomer = int(input('enter nomer for Alex: '))
Robert_nomer = int(input('enter nomer for Robert: '))
add_nomera(kontackti, "Ben", Ben_nomer)
add_nomera(kontackti, "Alice", Alice_nomer)
add_nomera(kontackti, "Nick", Nick_nomer)
add_nomera(kontackti, "Alex", Alex_nomer)
add_nomera(kontackti, "Robert", Robert_nomer)

poisk_contacta(kontackti, Ben_nomer)
"""......."""