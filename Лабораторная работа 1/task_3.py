list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
n =int(len(list_players)/2)
team1 = list_players[0:n]
team2 = list_players[n:]
print(team1)
print(team2)