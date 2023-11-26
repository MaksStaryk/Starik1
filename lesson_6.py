import math
"""task 1"""
def step(x):
    print(x,"raven =", x**2)
for a in range(1,10+1):
    step(a)
"""task 2"""
def kratnie_5_3():
    numbers = [ x for x in range(100,1000) if x % 3 == 0 and x % 5 == 0]
    return numbers
print(kratnie_5_3())
"""task 3"""


def tvoi_chisla(a, b, c):
    for x in range(a, b + 1):
        print(x ** c, end=' ')


a, b, c = input('enter value:').split()
a = int(a)
b = int(b)
c = int(c)
tvoi_chisla(a, b, c)
print()
"""task 4"""
print('task 4')
def sum_neighbors(numbers):
    num_list = list(map(int, numbers.split()))


    if len(num_list) == 1:
        return num_list[0]


    result_list = [num_list[i - 1] + num_list[(i + 1) % len(num_list)] for i in range(len(num_list))]

    return ' '.join(map(str, result_list))


some_numbers = "1 3 5 6 10"
output_result = sum_neighbors(some_numbers)
print(output_result)
"""task 5"""
print('task 5')
def little_chislo(s):
    minimal = 10
    while s > 0:
        d = s % 10
        if d < minimal:
            minimal = d
        s = s //10
    return minimal

a = 456
print(little_chislo(a))
print()
"""task 6"""
print('task 6')


def distance(x1,y1,x2,y2):
    return math.sqrt(( x2 - x1 )**2 + ( y2 - y1 )**2)

x1 = float(input('enter x1: '))
y1 = float(input('enter y1: '))
x2 = float(input('enter x2: '))
y2 = float(input('enter y2:' ))

result = round(distance(x1,y1,x2,y2),2)
print(f'Расстояние между точкой {x1},{y1} and {x2},{y2}: {result}')
print()

"""task 8"""
print('task 8')
def poisk_chisla(x):
    for a in range(x, x + 10):
        if a % 5 == 0 and a >= 0:
            print(a)
            break

x = int(input('enter number:'))
poisk_chisla(x)

"""task 9"""
print('task 9')
def sortirovka(lst):
    i = 0
    while i < len(lst):
        if lst[i] % 2 ==0:
            lst[i] //=2
            i += 1
        else:
            del lst[i]

some_list= [ 2,6,1,56,7]
sortirovka(some_list)
print(some_list)