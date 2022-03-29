# version 0.06, March 29 2022
#   - Added option to add time, and lengh of sets to make presentation better for enduser.
#   - Code a bit messy. Needs a cleanup, will happen later.
#
# version 0.05, March 28 2022
#   - gerhard fixed bug with two stages, now can add any number of players.
#
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


print("")
attending = input("How many players attending? (input number): ")

start_time = (input("Event start time? (input XXXX): "))
hour = int(start_time[0:2])
minute = int(start_time[2:])

set_length = int(input("Time between matches? (input XX mins): "))

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
    global hour, minute
    match_no = 1
    print("")
    for combo in combos:
        if minute >= 60:
            hour += minute // 60
            minute %= 60
            hour %= 24
                
        print(f'\t[{str(hour).rjust(2, "0")}:{str(minute).rjust(2, "0")} | Match {match_no}]: {combo[0].upper()} VS. {combo[1].upper()}\n')
        match_no += 1
        minute += set_length
    return

def two_stages(players):
    global hour, minute
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

    print("\n\tTime  | Left\t\t\t\t | Right")
    print("\t-------------------------------------------------------------")
    
    for i in range(0, len(matches), 2):
        p1 = matches[i][0]
        p2 = matches[i][1]
        
        if minute >= 60:
            hour += minute // 60
            minute %= 60
            hour %= 24        

        try:
            p3 = matches[i + 1][0]
            p4 = matches[i + 1][1]
        except IndexError:
            print(f'\t{str(hour).rjust(2, "0")}:{str(minute).rjust(2, "0")} | {p1.upper()} VS. {p2.upper()}\n')
            return
        
        left_lenght = len(p1 + p2)
        
        if left_lenght <= 7:
            tabs = '\t\t\t'
        elif left_lenght <= 17:
            tabs = '\t\t'
        elif left_lenght <= 23:
            tabs = '\t'
        elif left_lenght <= 31:
            tabs = ' '
        else:
            tabs = ' soo long names it screws up the presentation, so lets screw it up some more! '
        
        if minute >= 60:
            hour += minute // 60
            minute %= 60
            hour %= 24
        
        print(f'\t{str(hour).rjust(2, "0")}:{str(minute).rjust(2, "0")} | {p1.upper()} VS. {p2.upper()} {tabs} | {p3.upper()} VS. {p4.upper()}\n')
        minute += set_length
        

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

     
            
    



