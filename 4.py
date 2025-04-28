"""4. Удалить из текста все последовательности символов, заключенный в
круглые скобки. Предполагается, что количество открывающих и
закрывающих скобок совпадает, скобки расставлены правильно и
вложенных скобок нет."""

text = input()
result = []
brackets = False

for char in text:
    if char == '(':
        brackets = True
    elif char == ')':
        brackets = False
    elif not brackets:
        result.append(char)

print(''.join(result))
