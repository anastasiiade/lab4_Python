"""2. Дана строка, в которой записаны три слова через запятую. Изменить
последовательность слов в строке на обратную."""

s = input()

words = [
    word.strip()
    for word in s.split(',')
]

reversed_w = words[::-1]
result = ', '.join(reversed_w).lstrip()
print(result)
