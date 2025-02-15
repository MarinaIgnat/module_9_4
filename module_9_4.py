#Lambda-функция:

first = 'Мама мыла раму'
second = 'Рамена мало было'

#Функция get_advanced_writer возвращает функцию write_everything.
result = list(map(lambda x, y: x == y, first, second))
print(result)

#Замыкание:

#Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
def get_advanced_writer(file_name):
    #Внутри этой функции, напишите ещё одну - write_everything(*data_set), где *data_set - параметр принимающий
    # неограниченное количество данных любого типа.
    def write_everything(*data_set):
        #Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
        with open(file_name, 'a', encoding='utf8') as file:
            for data in data_set:
                file.write(str(data) + '\n')
    #Функция get_advanced_writer возвращает функцию write_everything.
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Метод __call__:

#Для случайного выбора с одинаковой вероятностью для каждого данного в коллекции можете использовать функцию
# choice из модуля random.


import random


#Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
class MysticBall:
    def __init__(self, *words):
        self.words = words

    #В этом классе также определите метод __call__ который будет случайным образом выбирать слово
    # из words и возвращать его.
    def __call__(self):
        return random.choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())


