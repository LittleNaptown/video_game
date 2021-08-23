import time

time.sleep(1)
print("ENTER PLAYER NAME")

playername=input()
time.sleep(3)
print(f"Welcome {playername}, to the Gold Rush Saloon.")

print("Y=Continue N=Quit Game")
game_action=input()
if game_action == "N":
      exit()
else:
    if game_action == "n":
        exit()

# opening statment
print("Bartender:Well your a new face, grab a seat and stay a while, take a look at my store, or take up a bounty and go slay some monsters.")

while 1==1:
    print("1=Grab a seat 2=Browse shop 3=Take a bounty 4=Leave")
    game_action=input()
    if game_action == "1":
        print("you grabed a seat in the corner")
    if game_action == "2":
        print(""" 1 Sword Upgrade= 250 Gold
        2 Healing Ointment= 25 Gold
        3 Arrows X5= 10 Gold
        4 Bow Upgrade= 250 Gold
        5 Long Bow= 500 Gold
        6 Exit Shop""")
        
# 3) take a bounty
    if game_action == "3":
        print(""" -------------------------------------------
|.     Bouny 1    |.     Bounty 2  |.    Bounty 3   | 
|.  Monster lvl 1 |.  Monster lvl 2|.  Monster lvl 3|
|.      Reward    |.     Reward    |.    Reward     |
|. 25 XP  25 Gold |. 45 Xp  45 Gold|.65 XP.  65 Gold|
|.                |.               |.               |
|. Possible reward|.Possible Reward|.Possible Reward|
|. Wooden Chest   |.  Silver chest |. Gold chest    |
--------------------------------------------""")
        game_action=input()
        if game_action == "1":
            print ("YOU TRACKED A BLUE AND RED STRIPPED GOLIATH THROUGH THE FOGGY FOREST AND WHEN YOU BOTH REACH AN OPENING IN THE FOREST, YOU DECIDE TO ENGAGE THE FIGHT BEFORE T EVADES YOU THROUGH THE TREE LINE")
        if game_action == "2":
            print("YOU TRACKED A GREEN AND SILVER STRIPPED GOLIATH NEAR THE ENTRACE OF A CAVE WHERE YOU DECIDE TO ENGAGE IN THE FIGHT BEFORE IT CRAWL INTO THE CAVE AND YOU LOSE IT TO DARKNESS")
        if game_action == "3":
            print("YOU TRACKED A PURPLE AND BLACK STRIPPED GOLIATH TO THE TOP OF A MOUNTAIN WHEN YOU DECIDE TO ENGAGE THE FIGHT BEFORE IT ESCAPES OVER THE MOUNTAIN TOP ")

# 4) leave tavern            
    if game_action == "4":
        print("YOU STEPPED OUTSIDE. Y= REENTER N=GAME OVER")
     game_action=input()
        if game_action == (Y):
            print("YOU RENTERED THE TAVERN")
        else:
             if game_action == "N":
        exit()
