"""
1. Напишите программу подсчета букв ‘a’ в строке «abrakadabra».

2. Из строки «abrakadabra» удалите все сочетания «ab».

3. Напишите программу определения слова палиндрома (это слова, которые одинаково читаются в обоих направлениях, например, анна, abba и т.п.).
Слово вводится с клавиатуры.

4. Напишите программу определения количества вхождений фраз «ra» в слове «abrakadabra».

5. Разделите введенное с клавиатуры предложение на слова (слова разделяются пробелом).
"""
#++++++++++++++++++++++++++++ Задание 1 Вариант 1 +++++++++++++++++++++++++++++++++++++
'''
1. Напишите программу подсчета букв ‘a’ в строке «abrakadabra».
'''
word = "abrakadabra"    # Создаем переменную с искомым словом
counter = 0             # Создаем счетчик

for letter in word:     # Перебираем переменную
    if letter == "a":   # Если находим а то увеличиваем счетчик на 1
        counter += 1

print(f"Букв а в слове {counter}" + '\n')   # Выводим полученные результат

#++++++++++++++++++++++++++++ Задание 1 Вариант 2 +++++++++++++++++++++++++++++++++++++

print(word.count('a'), '\n') # Данная функция отсчитывает количество букв а в слове

#++++++++++++++++++++++++++++ Задание 2 +++++++++++++++++++++++++++++++++++++

'''
2. Из строки «abrakadabra» удалите все сочетания «ab».
'''

print(word.replace('ab', '') + '\n')    # Функция находит символы которые ей передаются 1 аргументом, и заменяет его на второй.

#++++++++++++++++++++++++++++ Задание 3 +++++++++++++++++++++++++++++++++++++

'''
3. Напишите программу определения слова палиндрома (это слова, которые одинаково читаются в обоих направлениях, например, анна, abba и т.п.). 
Слово вводится с клавиатуры.
'''

word_pal = "анна"   # Создаем переменную с искомым словом
revers_word: str = word_pal[::-1]   # Делаем реверс слова
print(revers_word)      # Проверка реверса

if word_pal != revers_word: # Проверяем буквы основного слова и реверсивного слова
    print(f"слово {word_pal} не является палиндромом \n")  # Выводим полученные результат
else:
    print(f"слово {word_pal} является палиндромом \n")     # Выводим полученные результат

#++++++++++++++++++++++++++++ Задание 4 +++++++++++++++++++++++++++++++++++++

'''
4. Напишите программу определения количества вхождений фраз «ra» в слове «abrakadabra».
'''

print(f"фраз ra в слове {word} = {word.count('ra')} \n")    # Выводим полученные результат через функцию ra

#++++++++++++++++++++++++++++ Задание 5 +++++++++++++++++++++++++++++++++++++

'''
Разделите введенное с клавиатуры предложение на слова (слова разделяются пробелом).
'''

sentence = input('Введите предложение: ')   # Вводим предложение
word_len: len = sentence.split(' ')         # Вводим телефонный номер

for num, word in enumerate(word_len):       # Использую функцию enumerate чтобы каждое слово было пронумеровано
    print(f"{num}  {word}")                 # Выводим полученные результат

