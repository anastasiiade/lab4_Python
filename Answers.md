```python
# Запрашиваем у пользователя ввод строки
user_input = input("Введите строку: ")

# Приводим строку к нижнему регистру для удобства сравнения
lowercase_string = user_input.lower()

# Задаем набор гласных букв для проверки
vowel_letters = {'a', 'e', 'i', 'o', 'u'}

# Инициализируем счетчик гласных
vowel_count = 0

# Перебираем каждый символ в строке
for character in lowercase_string:
    # Проверяем, является ли символ гласной буквой
    if character in vowel_letters:
        # Увеличиваем счетчик при совпадении
        vowel_count += 1

# Выводим итоговый результат
print(f"Количество гласных букв в строке: {vowel_count}")
```
==================================
```python
# Получаем строку от пользователя
original_string = input("Введите строку: ")

# Разбиваем строку на слова по пробелам
words_list = original_string.split(' ')

# Создаем список для перевернутых слов
reversed_words = []

# Обрабатываем каждое слово в списке
for word in words_list:
    # Переворачиваем слово с помощью среза [::-1]
    reversed_word = word[::-1]
    # Добавляем перевернутое слово в новый список
    reversed_words.append(reversed_word)

# Собираем перевернутые слова обратно в строку
result_string = ' '.join(reversed_words)

# Выводим итоговый результат
print(f"Перевернутая строка: {result_string}")
```
