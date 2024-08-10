# Домашняя работа по уроку "Пространство имен."

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызов inner_function внутри test_function
    inner_function()


# Вызов test_function
test_function()

# inner_function() #вызов функции не доступен, она не взоне действия
