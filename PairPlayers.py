import itertools

players = ['Diggs', 'Ivory', 'Whitemonster', 'Milo', 'Bergtroll']

players_combo = itertools.combinations(players, 2)

for combo in players_combo:
    print(combo)
