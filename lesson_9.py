"""task 1"""
class Chisla:
     chislo_1 = 6
     chislo_2 = 112

     def ekran(self):   #вывод на экран chislo_1 and chislo_2
         print(f'chislo 1: {Chisla.chislo_1}')
         print(f'chislo 2: {Chisla.chislo_2}')

     def change(self):  # изменяем chislo_1 and chislo_2
         self.chislo_1 = self.chislo_1 + 34
         self.chislo_2 = self.chislo_2 + 1000
         print(f'izmen chislo 1 : {self.chislo_1}')
         print(f'izmen chislo 2 : {self.chislo_2}')

     def sum(self):     # суммируем chislo_1 and chislo_2
         return print(f'сумма chislo 1 + chislo 2: {self.chislo_1 + self.chislo_2}')


     def rock_num(self):    # вывод ниабольшего числа из chislo_1 or chislo_2
         if self.chislo_1 > self.chislo_2:
             print(self.chislo_1)
         else:
             print(self.chislo_2)

chisla = Chisla()
chisla.ekran()          #вывод атрибутов на экран
Chisla.change(chisla)   #изменение атрибутов
chisla.sum()    # сумма chislo_1 + chislo_2
chisla.rock_num() #наибольшее из чисел

"""task 2"""


class Counter:
    my_counter = 0

    def __int__(self, start_value):
        self.start_value = start_value
        start_value = Counter.my_counter


    def up(self):
        Counter.my_counter += 1

    def down(self):
        Counter.my_counter -= 1

    def ekran(self):
        print(Counter.my_counter)

print('если вы вводите от 0 до 5, то счетчик увеличивается на 1, любое другое -1')

our_counter = Counter()
while Counter.my_counter < 20 and Counter.my_counter > -20:

    user_point = int(input('your value: '))
    if user_point > 0 and user_point <= 5:
        our_counter.up()
    else:
        our_counter.down()
    our_counter.ekran()
print(f'счетчик получил максимальное значение {Counter.my_counter}')

# код сыроват, хотелось добавить break, continue для большей функциональности
#все выходные был в разъездах

"""task 3"""
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Spar:
    def __init__(self):
        self.value = []

    def add_food(self, foods):
        self.value.append(foods)
        print(f'dobavlen {foods.name} and price ${foods.price}')
    def poisk_foods(self, eat):
        for foods in self.value:
            if foods.name == eat:
                return foods
    def udal_foods(self,eat):
        for food in self.value:
            if food.name == eat:
                self.value.remove(food)


spar = Spar()

your_product1 = Product('Orange', 1.56)
your_product2 = Product('Apple', 0.67)
your_product3 = Product('Eggs', 4)
your_product4 = Product('Halva', 0.99)


spar.add_food(your_product2)
spar.add_food(your_product1)
spar.add_food(your_product3)
spar.add_food(your_product4)


my_poisk = spar.poisk_foods(input('enter food:'))
if my_poisk:
    print(f"{my_poisk.name} naiden")
else:
    print('net takogo')

spar.udal_foods('Halva')

my_poisk = spar.poisk_foods(input('enter food:'))
if my_poisk:
    print(f"{my_poisk.name} naiden")
else:
    print('net takogo')