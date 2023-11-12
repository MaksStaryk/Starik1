"""task 3"""
some_string = '192.168.0.1'
some_string2 = some_string.replace('.','')
some_string3=  int(some_string2[:4:])
some_string4 = int(some_string2[4::])
print()

"""task 4"""
print(some_string3 + some_string4)
print()
some_word = ('predecessore')
print(some_word.count('e'))
print()
