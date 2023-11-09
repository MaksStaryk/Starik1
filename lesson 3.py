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