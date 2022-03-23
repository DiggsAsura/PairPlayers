# version 0.01.
#
# This program takes a list of players, and return all the possible combinations, in groupings
# of 2. 
#
# I made this quick and dirty for helping organizing the matchups in Classic Tetris League (CTL)
# where we needed to sort out all the matches done in a restream.
#
# Might work more on this, to make it useable for more Restreamers or match organizers, as well
# adding options for X and Y... 
#
# Diggs


import itertools

players = ['Diggs', 'Ivory', 'Whitemonster', 'Milo', 'Bergtroll']

players_combo = itertools.combinations(players, 2)

for combo in players_combo:
    print(combo)
