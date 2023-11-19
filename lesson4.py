import math
"""start task 1"""
print('start task 1')
a = -1
b = 21
c = 3

print( a < 0 ,b < 0,c < 0)
print()
"""start task 2"""
print('start task 2')
n = 12
k = 24
if n //2 *2 ==n and k //2 *2 == k:
    print('есть четность')
else:
    print('нет четности')
print()
"""start task 3"""
print('start task 3')
a = 7
d = 0
for q in range(1,a+1):
    if q % 2 ==0:
      d +=1
print('кол-во четных:',d)
e = 4
r = 0
for w in range(1,e+1):
    if w % 2 == 0:
       r += 1
print('кол-во четных:',r)

w = 10
t =0
for q in range(1,w+1):
    if q % 2 ==0:
      t +=1
print('кол-во четных:',t)
print('общее количество четных',d+r+t)
print()
"""start task 4"""
print('start task 4')
v = '99'
q = int(v[0])
w = int(v[1])
if q + w <10:
    print('Da')
else:
    print('Net')
print('task 5')
a = 10
b = 1
while a <= 29:
    print(b,'раз:', 10,)
    a += 1
    b += 1
print()
''''task 6'''
print('task 6')
some_number_6 = 7
i = 1
while i <=some_number_6:
    print((pow(i,3)), end=' ')
    i +=1
print()
"""start task 7"""
print('start task 7')
a = 5
d =6
q = 1
while q <= 20:
    a = a*d
    d +=1
    q +=1
    print(a)
print(a)
print()
"""start task 8"""
print('start task 8')
n =14
a = 1
b = 3

while a < n :
    print(a, end=' ')
    a +=b
    b += 2
print()
"""start task 9"""
print('start task 9')
a = 96
minimum = 10
while a > 0:
    d = a %  10
    if d < minimum:
        minimum = d
    a //= 10
print('наименьшая цифра:', minimum)
print()
"""start task 10"""
print('task 10')
year = int(input('enter a year:'))

if ( year % 4 ==0 and year % 100 !=0) or year % 400 ==0:
    print('год  високосный')
else:
    print('год не високосный')