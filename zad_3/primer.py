import math
    

def script(text):
    text_len = len(text)
    text_len_sqrt = int(math.sqrt(text_len))
    while text_len > text_len_sqrt * text_len_sqrt:
        text_len_sqrt+=1
    matrix = []
    counter_rows = 0

    while counter_rows < text_len_sqrt:
        appender = []
        for index in range(0, text_len_sqrt):
            number = text_len_sqrt * index + counter_rows
            if number < text_len:
                appender.append(text[number])
            else:
                appender.append(' ')
        matrix.append(appender)
        counter_rows += 1

    text_out = ""
    for index in range(0, text_len_sqrt):
     for jindex in range(0, text_len_sqrt):
            text_out+=str(matrix[index][jindex])

    return text_out


#Шифровка
user_text = input("Введите текст: ")

output_s = script(user_text)

print(output_s)

#Расшифровка
output_r = script(output_s)

print(output_r)