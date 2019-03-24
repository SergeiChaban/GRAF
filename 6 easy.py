# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go (self):
        print ('Машина поехала')

    def stop (self):
        print('Машина остановилась')

    def turn_right (self):
        print('Машина повернула на право')

    def turn_left (self):
        print('Машина повернула на лево')

TownCar = Car ('60', 'Blue', 'Toyota', False)
SportCar = Car ('160', 'Red', 'Lamborgini', False)
WorkCar = Car ('60', 'Yellow', 'Ford', False)
PoliceCar = Car ('120', 'White', 'Chevrolet', True)

