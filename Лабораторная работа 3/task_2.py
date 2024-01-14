# TODO Напишите функцию find_common_participants
def find_common_participants(f_group, s_group, sep = ","):
    c_list = list(set(f_group.split(sep)).intersection(s_group.split(sep)))
    return sorted(c_list)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))