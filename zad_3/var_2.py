import math

def fix_length(text_len, text_len_sqrt):
    while text_len > text_len_sqrt * text_len_sqrt:
        text_len_sqrt+=1
    return text_len_sqrt

#Шифровка
user_text = input("Введите текст: ")
text_len = len(user_text)
text_len_sqrt = int(math.sqrt(text_len))
text_len_sqrt = fix_length(text_len, text_len_sqrt)
matrix = []
counter_rows = 0

while counter_rows < text_len_sqrt:
    appender = []
    for index in range(0, text_len_sqrt):
        number = text_len_sqrt * index + counter_rows
        if number < text_len:
            appender.append(user_text[number])
        else:
            appender.append(' ')
    matrix.append(appender)
    counter_rows += 1

text_out = ""
for index in range(0, text_len_sqrt):
    for jindex in range(0, text_len_sqrt):
        text_out+=str(matrix[index][jindex])

print(text_out)

#Расшифровка
user_text = text_out
text_len = len(text_out)
text_len_sqrt = int(math.sqrt(text_len))
text_len_sqrt = fix_length(text_len, text_len_sqrt)
matrix = []
counter_rows = 0

while counter_rows < text_len_sqrt:
    appender = []
    for index in range(0, text_len_sqrt):
        number = text_len_sqrt * index + counter_rows
        if number < text_len:
            appender.append(user_text[number])
        else:
            appender.append(' ')
    matrix.append(appender)
    counter_rows += 1

text_out = ""
for index in range(0, text_len_sqrt):
    for jindex in range(0, text_len_sqrt):
        text_out+=str(matrix[index][jindex])

print(text_out)
