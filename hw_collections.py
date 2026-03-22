# 1 - Написать программу, которая получает на вход строку и возвращает словарь, где:

user_string = input('Введите символы: ')

result = {}

for i in user_string:
    result[i] = user_string.count(i)
print(result)



# 2 - Дана строка текста (или введённая через консоль). Программа должна вернуть новую строку, в которой порядок слов будет обратным.


user_string = input('Введите текст: ')

user_list = user_string.split()

reverse_list = []

for i in user_list:
    reverse_list.append(i)

reverse_list.reverse()

print(' '.join(reverse_list))



#3 Написать программу, которая удаляет из списка все дубликаты, сохранив исходный порядок элементов.

user_string = input('Введите текст: ')

draft_list = user_string.split()

result = []

for i in draft_list:
    if i not in result:
        result.append(i)
print(result)




#4 Даны три (или больше) списка с объектами. Программа должна создать новый список, содержащий все уникальные элементы — каждый объект встречается только один раз.

letters = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']

numbers = ['1', '2', '3', '4', '5', '1', '2', '3', '4', '5']

fruits = ['apple', 'apple', 'orange']

result = []

all_objects = letters + numbers + fruits

for i in all_objects:
    if i not in result:
        result.append(i)


print(result)



#5 Дана строка текста (или введённая через консоль). Программа должна вернуть словарь с четырьмя ключами:
# "гласные",

# "согласные",

# "цифры",

# "пунктуация".

# Значения — количество символов каждого типа в строке.


user_string = input('Введите текст на русском языке или цифры: ')


vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
punctuation = ['.', ',', '!', '?', ':', ';', '-', '—', '(', ')', '"', "'", '...']


keys = ['гласные', 'согласные', 'цифры', 'пунктуация']


count_vowels = 0
count_consonants = 0
count_digits = 0
count_punctuation = 0


for i in user_string:  
    if i.lower() in vowels:
        count_vowels += 1
    elif i.lower() in consonants:
        count_consonants += 1
    elif i in digits:
        count_digits += 1
    elif i in punctuation:
        count_punctuation += 1


result = {
    keys[0]: count_vowels,
    keys[1]: count_consonants,
    keys[2]: count_digits,
    keys[3]: count_punctuation
}

print(result)



















