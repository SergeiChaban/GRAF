# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def unit_name (self):
        self.name = input('Введите имя: ')

    def unit_health (self):
        self.health = 100
        print(self.health)

    def unint_damage (self):
        self.damage = 50
        print (self.damage)

    def unint_armor (self):
        self.armor = 50
        print (self.armor)


class Enemy(Person):
    self.armor = armor


class Player(Person):

attack(player, enemy)
print(enemy['health'], player['health'])

player = Person('', 100, 50)
enemy = Person('', 100, 50)

print (player.name)


def attack(self, who_attack, who_defend):
    def attack(self, who_attack, who_defend):
        self.who_defend['health'] -= who_attack['damage']
