fruit = {"title": "Apple", "price": 0.9}
# Создаем словарь с именованными полями товара.
print(fruit["title"], fruit["price"])
# Достаем значения по названиям ключей словаря.
pair = ("Apple", 0.9)
# Создаем кортеж, в котором название стоит первым, а цена вторым.
print(pair[0], pair[1])
# Достаем элементы кортежа по индексам 0 и 1.
fruits = [("Orange", 2.3), ("Apple", 0.9), ("Banana", 2.4)]
# Создаем список из трех пар, как в архивном примере.
print(type(fruit).__name__, type(pair).__name__)
# Показываем, что словарь и кортеж имеют разные типы.
print(type(fruits).__name__)
# Проверяем, что внешняя коллекция пар является списком.
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruit["price"] + fruit["price"])