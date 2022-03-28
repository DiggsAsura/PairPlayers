# PairPlayers v0.05

### Introduction
PairPlayers was made in a hurry where we needed to sort out all possible combinations of
matchups in Classic Tetris League (CTL), before going live. 

This is an extremly simple script that will take a list of players, and return
all the combinations, in groupings of 2. 

### Requirements and usage
**Python 3.6+ is required to run properly**  
  
**How to run**  
1. Download PairPlayers.py
2. From a terminal/command-prompt within the folder: python PairPlayers.py


### Update history
v0.05 release (March 28 2022)  
- gerhardadler fixed logic to handle any amount of players. Big kudos!

---

v0.04 release (March 28 2022)  
- Improved logic. Less then 4 players? 1 stage is only option.  

---

v0.03 release (March 28 2022)  
This is quite a big one. Some big brain logic added by gerhardadler to handle a 4 way restream
in CTL. Means, two matches can happen without the returned lists have the same player on 
both stages at the same time.

  **Updates**:
  - Big brain logic for 4 way by gerhardadler, THANK YOU!!
  - Added logic for handling 1 or 2 stages
  - Facelift on presentation! Way more readable for user

  **Known issues**:
  - issue some total number of players! upward until 6 it's ok, which should be good enough for
    CTL (Classic Tetris League). Workin on it now (thanks again gerhardadler!)
  - minor issue which will be updated soon: if less then 4 players, there should be no choice
    for one or two stages. should just return single stage combos. 

---

v0.02 release (March 27 2022)
  - The script now takes inputs, so don't have to type them into the
    actual script yourself.

---

### Todos
- Actually make it useful for anyone (for now only a script)
- Make it a web app?

*PS! I'm still learning Python, some of those todos might or might nothappen in near future!*

