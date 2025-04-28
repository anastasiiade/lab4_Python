"""1. Дана цепочка символов вида "число1*число2+число3*число4".
Вычислить числовое значение выражения и напечатать."""

text = input()

def calculate_part(part):
    a, b = map(int, part.split('*'))
    return a * b

result = sum(calculate_part(part) for part in text.split('+'))
print(result)
