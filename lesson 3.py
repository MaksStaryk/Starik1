"""task 1"""
some_word = 'призрак'
print(some_word[2])
print(some_word[-2])
print(some_word[:6:])
print(some_word[0:5:])
print(some_word[2::2])
print(some_word[1::2])
print(some_word[::-1])
print(some_word[::-2])
print(len(some_word))
print("the end task 1")
"""task 2"""
print()
print("start task 2")
print((some_word[0]) == (some_word[-1]))
print()
print('start task 3')
name = 'машина'
work_name = name[1] + name[2] +name[3]
print(work_name)
print()
"""start task 4"""
print('start task 4')
fruit ="яблоко"
print(fruit[1:5:])
print(fruit[5:2:-1])
print()
"""start task 5"""
print('start task 5')
full_name = "Иванов Иван"
print(full_name[7::]+" "+ full_name[0:6:])
print()
"""start task 6"""
print("start task 6")
full_name = "Иванов Иван"
print(full_name)
print('является ли строка',full_name,'палиндромом=' ,full_name[::] == full_name[::-1])
print()
"""start task 7"""
print('start task 7')
names= ["andrei", "pasha", "viktor"]
print(names[1])
print()
"""start task 8"""
print('start tast 8')
first_word = 'employ'
second_word = 'employment'
print(second_word.startswith(first_word))
print()
"""start task 9"""
print("start task 9")
some_word = 'frogfrogfrog'
some_word2= some_word.replace('f','a',1)
print('индекс второй f:',some_word2.index('f'))
print()
"""start task 10*"""
print("task 10*")
school_classes = {'1a':15, '2a':15, '3a':15, '4a':15, '5a':15, '6a':15, '7a':15, '8a':15, '9':{'a':15, 'b':15}, '10a':15}
print('task 10a')
child_add = 5
school_classes['1a'] += child_add
print(school_classes['1a'])
print()
print('task 10б')
school_classes['9b'] = '15'
print('добавлен класс 9b',school_classes['9b'])
print()
"task 10в"
del school_classes['2a']
print()
print('task 10г')
nine_clasess = school_classes.get('9')
nine_clasess1 = nine_clasess.values()
print(sum(nine_clasess1))

