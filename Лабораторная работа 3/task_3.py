# TODO  Напишите функцию count_letters
def count_letters(text):
    text1 = text.lower()
    Dict = {}
    for i in range(len(text1)):
        if text1[i].isalpha() == True:
            if text1[i] in Dict.keys():
                Dict[text1[i]] = Dict.get(text1[i])+1
            else:
                Dict[text1[i]] = 1
        else:
            continue
    return Dict

# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict1):
    dict2 = {}
    sum_let = sum(dict1.values())
    for i in dict1.keys():
        dict2[i] = round(dict1.get(i)/sum_let, 2)
    return dict2

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
a = calculate_frequency(count_letters(main_str))

for key, value in a.items():
    print(key, value)


