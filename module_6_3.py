
class Horse:

    def __init__(self):
        self.x_distance = 0   # пройденный путь
        self.sound = 'Frrr'  #  звук, который издаёт лошадь

    def run(self, dx):
        self.x_distance += dx  # изменение дистанции, увеличивает x_distance на dx

class Eagle:

    def __init__(self):
        self.y_distance = 0  # высота полёта
        self.sound = 'I train, eat, sleep, and repeat'  # звук, который издаёт орёл(отсылка)


    def fly(self, dy):
        self.y_distance += dy  #  изменение дистанции, увеличивает y_distance на dy.

class Pegasus(Horse, Eagle):  # наследие идет от правого к левому
    def __init__(self):  # создаем инит обьекта
        Horse.__init__(self)    # присваиваем данные класа Horse
        Eagle.__init__(self)    # периписываем однотипные методы на методы класса Eagle

    def move(self, dx, dy): # метод двойного изменения
        self.run(dx)
        self.fly(dy)


    def get_pos(self):   # возвращает текущее положение пегаса в виде кортежа (x_distance, y_distance) в том же порядке
        return (self.x_distance, self.y_distance)

    def voice(self): # выводим звук объекта
        print(self.sound)

# Код для проверки
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()