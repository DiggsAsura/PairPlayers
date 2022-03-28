# version 0.04, March 28 2022
# - Updated logic where it's less then 4 players, just one stage is selected automatically.
#
# version 0.03, March 28 2022 
# Big thanks to gerhard_adler for solving some cruical logic!
#
#   - Added: logic for handle single or double matchups
#
#   - Added: logic for splitting into two "arenas", so two matchups can happen at the same
#            time, without having same players in both left and right arena at the same time.
#
#   - Added: Way better presentation of the actual matchups
#
#   - Known issues: 
#       - There are some issues with some number of matchups. 7, 12 etc.. Working on it with Gerhard.
#
# version 0.02
#
# - Updating to take inputs. 
#
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
import time

attending = input("How many players attending? (input number): ")
players = []
count = 1

# Populate players list
while (len(players) + 1) <= int(attending):
    player = input(f'Player {count}: ')
    players.append(player)
    count += 1


# Make a list with all the possible combinations of matchups.
combos = list(itertools.combinations(players, 2))

def one_stage(combos):
    match_no = 1
    print("")
    for combo in combos:
        print(f'\tMatch {match_no}: {combo[0]} VS. {combo[1]}\n')
        match_no += 1
    return

def two_stages(players):
    matches = []

    for i, value in enumerate(players):
        players[i] = [value, 0]

    # This loop takes the player list containing lists with playername and count as input.
    # ------------------------------------------------------------------------------------
    # For example:
    # players = [["player1", 0], ["player2", 0], ["player3", 0], ["player4", 0]]
    #
    # The count is used to make sure all players are used evenly throughout the matches.
    # This makes sure that a situation like this doesn't happen:
    # ------------------------------------------------------------------------------------
    # player1 vs player2 | player3 vs player4
    # player1 vs player4 | player2 vs player4
    # player1 vs player5 | player2 vs player3    Because of the earlier rows, player5 has
    # player1 vs player4 | player2 vs player5    to play two matches at the same time in
    # player3 vs player5 | player4 vs player5  - the last row...
    #
    # The output is matches, a list containing all the matches. They are in an order that 
    # allows them to be put in two columns.
    # ------------------------------------------------------------------------------------
    # For example:
    # matches = [
    #     ("player1", "player2"), ("player3", "player4"),
    #     ("player1", "player3"), ("player2", "player4"),
    #     ("player1", "player4"), ("player2", "player3")
    # ]

    for x in range(len(players) - 1):
        for y in players:
            if not y[1] == x:
                continue
            offset = x
            while True:
                for z in players:
                    if z[1] != offset:
                        continue
                    if y[0] != z[0] and (y[0], z[0]) not in matches:
                        matches.append((y[0], z[0]))
                        y[1] += 1
                        z[1] += 1
                        break
                else:
                    offset += 1
                    continue
                break

    print("\n\t| Left\t\t\t\t | Right")
    print("\t-------------------------------------------------------------")
    
    for i in range(0, len(matches), 2):
        p1 = matches[i][0]
        p2 = matches[i][1]

        try:
            p3 = matches[i + 1][0]
            p4 = matches[i + 1][1]
        except IndexError:
            print(f'''\t| {p1} VS. {p2}\n''')
            return
        
        left_lenght = len(p1 + p2)
        
        if left_lenght <= 7:
            tabs = '\t\t\t'
        elif left_lenght <= 15:
            tabs = '\t\t'
        elif left_lenght <= 23:
            tabs = '\t'
        elif left_lenght <= 31:
            tabs = ' '
        else:
            tabs = 'upds'
        
        print(f'''\t| {p1} VS. {p2} {tabs} | {p3} VS. {p4}\n''')

# 1 or 2 stages and print the results
# 1 stage is automatic if number of players is less then 4
if len(players) < 4:
    one_stage(combos)
else:    
    stages = input("One or two stages? (input 1 or 2): ")
    if stages == '1':
        one_stage(combos)
    elif stages == '2':
        two_stages(players)

     
            
    



