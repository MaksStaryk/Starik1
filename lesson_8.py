"""task 2"""


def start_file(file, chisla):
    with open(file, 'w') as file:
        file.write(' '.join(map(str, chisla)))


def read_file(file):
    with open(file, 'r') as file:
        num = [float(num) for num in file.read().split()]


def finish_file(file, proizved):
    with open(file, 'w') as file:
        file.write(f'proizved chisel: {proizved}')


chisla = [4, 2, 1, 6, 4, 5, 165, 76, 98, 112]
proizved = 1
for num in chisla:
    proizved *= num

new_file = 'input.txt'
new_file_2 = 'output.txt'  # где будут храниться произведения чисел

start_file(new_file, chisla)
read_file((new_file))
finish_file(new_file_2, proizved)

new_file_2 = open('output.txt', 'r')
print(new_file_2.read())
new_file_2.close()
"""task 7"""
stroka = "backer"

try:
    print(stroka[10])
except IndexError:
    print('net takogo indexa. repeat')
print()
"""task 8"""
def delit(a:int,b ="str"):
    return a/b
try:
    print(delit(4))
except TypeError:
    print('зачем делить на строку!!!!!!')
print()
"""task 10"""
lst = [1,3,4]

try:
    num = int(input('your index:'))
    lst.remove(num)
except ValueError:
    raise TypeError('net takogo elementa')