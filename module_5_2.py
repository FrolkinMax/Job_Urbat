# Задача "Developer - не только разработчик":
    
class House: # класс
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    
    def go_to(self, new_floor): # метод подъема на этаж
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1): # new_floor + 1 т.к. иначе будет подъем не включая указанный этаж 
                print(i)
        else:
            print("Такого этажа не существует")
    
    def __len__(self): # возвращаем количество этажей
        return(self.number_of_floors)
        
    def __str__(self): # возвращаем строку "Название: <название>, кол-во этажей: <этажи>".
        return(f"Название: {self.name}, кол-во этажей: {self.number_of_floors}.")
    
    
    
    
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))