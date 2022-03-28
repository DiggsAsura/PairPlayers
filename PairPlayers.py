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

def two_stages(combos):
    left = combos[:len(combos)//2]
    right = combos[len(combos)//2:]

    results = []

    for x in range(len(left)):
        for y in range(len(right)):
            for z in left[x]:
                if z in right[(x + y) % len(right)]:
                    break
            else:
                rightAppend = right.pop((x + y) % len(right))
                results.append((left[x] , rightAppend))
                break
        else:
            exit("Well... This should not happen. Call Gerhard.")

    print("\n\t| Left\t\t\t\t | Right")
    print("\t-------------------------------------------------------------")
    
    for i in results:
        p1 = i[0][0]
        p2 = i[0][1]
        p3 = i[1][0]
        p4 = i[1][1]
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

    if len(right) != 0:
        print(f'''\t| {right[0][0]} VS. {right[0][1]}\n''')     
    return

# 1 or 2 stages and print the results
stages = input("One or two stages? (input 1 or 2): ")
if stages == '1':
    one_stage(combos)
elif stages == '2':
    two_stages(combos)

     
            
    



