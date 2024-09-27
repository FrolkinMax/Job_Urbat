
class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white'] # список допустимых цветов для окрашивания

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner                  # владелец транспорта. (владелец может меняться)
        self.__model = model                # модель (марка) транспорта. (мы не можем менять название модели)
        self.__color = color                # название цвета. (мы не можем менять цвет автомобиля своими руками)
        self.__engine_power = engine_power  # мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)


    def get_model(self) -> str:  # возвращает строку: "Модель: <название модели транспорта>"
        return f"Модель: {self.__model}"

    def get_horsepower(self) -> int:  # возвращает строку: "Мощность двигателя: <мощность>"
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self) -> str:  # возвращает строку: "Цвет: <цвет транспорта>"
        return f"Цвет: {self.__color}"

    def set_color(self, new_color: str):
        if new_color.lower() in (color.lower() for color in self.__COLOR_VARIANTS):
            self.__color = new_color  #  принимает аргумент new_color(str)
        else:  # меняет цвет __color на new_color, если он есть в
            print(f"Нельзя сменить цвет на {new_color}")


    def print_info(self): # распечатывает результаты методов (в том же порядке)
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        super().__init__(owner, model, color, engine_power)


# Пример использования
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
