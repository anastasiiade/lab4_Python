"""5. Написать программу «Транскрипция английских букв». Программа в
строку с буквами английского алфавита после каждой буквы вставляет ее
транскрипцию на русском языке. Например, из строки ‘abc’ формируется
строка ‘a(эй)b(би)c(си)’. Выберите 10 любых букв английского языка."""

transcription = {
    'a': 'эй',
    'b': 'би',
    'c': 'си',
    'd': 'ди',
    'e': 'и',
    'f': 'эф',
    'g': 'джи',
    'h': 'эйч',
    'i': 'ай',
    'j': 'джей'
}

text = input("Введите английские буквы (a-j): ").lower()
result = []

for letter in text:
    if letter in transcription:
        result.append(f"{letter}({transcription[letter]})")
    else:
        result.append(letter)

print(''.join(result))
