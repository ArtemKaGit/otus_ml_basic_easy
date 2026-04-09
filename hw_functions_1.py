
#---------------------------------------------

# def summa(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result

# print(summa(1, 1, 1, 1, 1))
# print(summa(2, 2, 2, 2, 2))
# print(summa(1, 1, 1, 1, 1))

#---------------------------------------------


# def summa(*args, **kwargs):
#     result = 0
#     for i in args:
#         result += i
#     for i in kwargs.values():
#         result += i
#     return result

# print(summa(1, 1, 1, 1, 1))
# print(summa(a=10, b=100, c=10))


#---------------------------------------------

#Напиши функцию square(x), которая принимает число и возвращает его квадрат.


# def square(x):
#     return x * x


# try:
#     x = int(input('Введите число: '))  
#     print(square(x))
# except ValueError:
#     print ('Это не число!')

#---------------------------------------------

# Напиши функцию max_of_two(a, b), которая принимает два числа и возвращает большее из них. 
# Если числа равны — вернуть любое.

# def max_of_two(a: int, b: int):
#     if a > b:
#         return a
#     elif a < b:
#         return b
#     else:
#         return a, b
    
# try:
#     a = int(input('Введите первое число: '))
#     b = int(input('Введите второе число: '))
#     print(max_of_two(a, b))
# except ValueError:
#     print ('Это не числа!')
    
 #---------------------------------------------   
    
# Напиши функцию is_even(n), которая принимает число и возвращает строку:

# "Чётное" — если число делится на 2

# "Нечётное" — если не делится

# def is_even(x):
#     if x % 2 == 0:
#         return f'{x} - это четное число'
#     else:
#         return f'{x} - это нечетное число'
    
# try:
#     x = int(input('Введите число: '))
#     print(is_even(x))
# except ValueError:
#     print('Это не число')

#---------------------------------------------

# 1
# Написать функцию, которая принимает неограниченное количество чисел в виде позиционных аргументов 
# и ключевой аргумент — операцию над этими числами (сложение или умножение).
# Функция должна возвращать результат выполнения указанной операции.


# def my_func(*args: tuple[int | float], operation: str = 'add') -> int | float:
#     if not args:
#         return 'Ошибка аргумента'
    
#     if operation == 'add':
#             return sum(args)
#     elif operation == 'multiply':
#         result = 1
#         for i in args:
#             result *= i
#         return result
#     else:
#         return 'Ошибка операции'

# print(my_func(1, 2, 3, operation = 'some op'))
# print(my_func(1, 3, 10, operation = 'add'))
# print(my_func(1, 2, 3, operation = 'multiply'))
# print(my_func())
# print(my_func(1, 2, 3))

#---------------------------------------------

# 2 Написать функцию для ввода из консоли целого числа.

# Если введено не число, функция должна вывести соответствующее сообщение 
# и предложить ввести значение заново — до тех пор, пока пользователь не введёт корректное число.

# def get_integer():
#     """Запрашивает целое число, повторяет запрос при ошибке"""
#     while True:
#         user_input = input('Введите целое число: ')
        
#         # Проверяем на дробное число
#         if '.' in user_input:
#             print('Ошибка: Введено дробное число!')
#             print('Попробуйте снова.\n')
#             continue  # Начинаем цикл заново
        
#         # Проверяем на целое число
#         try:
#             number = int(user_input)
#             return number  # Успех!
#         except ValueError:
#             print('Вы ввели не число')
#             print('Попробуйте снова.\n')

# # Использование
# x = get_integer()
# print(f'Вы ввели целое число: {x}')

   
#---------------------------------------------

# 3 Написать функцию, которая создаёт абсолютный путь к файлу.

# Позиционные аргументы:

# название диска,

# неограниченное количество папок,

# имя файла (без расширения).


# Ключевые аргументы:
# ext — расширение файла,

# sep — разделитель (по умолчанию '/').


# Пример:
# full_path('c:', 'work', 'python', 'function', 'main', ext='py') ➜ 'c:/work/python/function/main.py'


# def my_path(disk, *folders, filename, ext=None, sep='/'):
#     path = disk
#     for folder in folders:
#         path = path + sep + folder
#     path = path + sep + filename

#     if ext:
#         path = path + '.' + ext
#     return path

# print(my_path('c: ', 'work', 'python', 'function', filename='main', ext='py'))

      
#---------------------------------------------

# 4. Написать функцию, которая принимает список, состоящий из объектов разных типов, и возвращает словарь, где:
# ключи — типы данных объектов;

# значения — списки объектов соответствующего типа.

# def group_by_type(items):
#     result = {}
#     for item in items:
#         type_name = type(item).__name__
#         if type_name not in result:
#             result[type_name] = []
#         result[type_name].append(item)
#     return result

# test_list = [1, 'hello', 3.14, 'world', [1,2,3], 42, True, None, (1,2)]
# print(group_by_type(test_list))











