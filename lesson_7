from functools import reduce
"""task 1"""
stroka_1 = 'hello world'
stroka_2 = ' '

podgotovka = lambda a,b:  stroka_1 in stroka_2
result = podgotovka(stroka_1, stroka_2)
if result:
    print('stroka naidena')
else:
    print('stroki net')
print()
"""task 2"""
chislo = int(input('enter (intiger) value: '))
check = lambda a: print('est chetnost') if a % 2 == 0 else print('net chetnosti')
checker = check(chislo)
print()
"""task 3"""
your_exit = lambda a: print(f'correct {a}') if a[0].isupper() else print('again')
stroka = str(input('enter(str) value: '))
stroka_v2 = ''.join(stroka.split())
your_exit(stroka_v2)
print()
"""task 4"""
def digits(n):
    if len(n) ==0:
        return   n
    else:
        return digits(n[1:]) + ' '+ n[0]
string = input('enter (string) value: ')
povtor_string = str(string)
print(digits(string))
"""task 5"""
def is_power(n):
    if n == 1:
        return True
    elif n % 2 ==0 and n !=0:
        return is_power(n//2)
    else:
        return False
print(is_power(32))
print()
"""task 6"""
from functools import reduce
my_number = 14623
my_number_str = str(my_number)
lst_number = list(map(int, my_number_str))
print(lst_number)
summa = reduce((lambda x,y: x + y), lst_number)
print(summa)
"""task 7"""
def time(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] vremja : {} second'.format(end-start))
    return wrapper

@time
def prostie_chisla():
    for num in range(2, 100):
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            print(num)
prostie_chisla()
print()
"""task 8"""
def passowrd(func):
    def wrepper():
        if user_password == system_password:
            func()
        else:
            print('repeat')
    return wrepper
@passowrd
def check():
    print('congratilation')
user_password = int(input('enter value(intiger): '))
system_password = 345
check()
