import json
import csv

"""task 1"""
def  add_symvol(file1,file2):
    with open(file1,'r') as file:
         new_file = file.readlines()
    symvol = [x.strip() +'!' for x in new_file]

    with open(file2,'w') as finish_file:
        finish_file.write('\n'.join(symvol))

file_1 ='11.txt'
file_2 = '112.txt'

add_symvol(file_1,file_2)
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

"""task 4 and 5"""
case = {
    10001 : ('Anna', 32),
    20002 : ('Sergei', 25),
    30003 : ('Pasha', 37),
    40004 : ('Liza', 33),
    50005 : ('Natali', 38)
}
json_case = 'case_1.json'

with open(json_case,'w',encoding='utf-8') as json_1 :
    json.dump(case,json_1, ensure_ascii=False, indent=4)
with open(json_case,'r') as json_case:
    names = json.load(json_case)
csv_file = 'person.csv'
with open(csv_file,'w', newline='', encoding='utf-8') as csv_1:
    poet = csv.writer(csv_1, delimiter=';')

    poet.writerow(['person', 'name', 'age'])

    for key, value in names.items():
        poet.writerow(['person', value[0], str(value[1])])
print(csv_file)


print(json_case)

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