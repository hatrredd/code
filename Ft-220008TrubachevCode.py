result = []
asd = 0
alphZ = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З","И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Ш", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]
alph = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
word = str(input("Введите слово/предложение на русском, которое хотите зашифровать: "))
sdvCo = int(input("Введите число, с каким сдвигом зашифровать: "))
while sdvCo < 0:
    sdvCo = int(input("Вы ввели некорректное число для сдвига, попробуйте ещё раз: "))
while sdvCo >= 33:
    sdvCo -= 33
for i in range (len(word)):
    if word[i] not in alph and word[i].lower() not in alph:
        result.append(word[i])
    elif word[i] in alphZ:
        s = alphZ.index(word[i])
        if abs((s + sdvCo)) - abs(len(alphZ)) >= 0:
            result.append(alphZ[abs(len(alphZ) - (s + sdvCo))])
        else:
            result.append(alphZ[s + sdvCo])
    else:
        s = alph.index(word[i])
        if abs((s + sdvCo)) - abs(len(alph)) >= 0:
            result.append(alph[abs(len(alph) - (s + sdvCo))])
        else: result.append(alph[s + sdvCo])
print(*result, sep="")