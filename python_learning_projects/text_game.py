NameD=input("What's your name ? ")
player_stats = {
    "name":"",
    "level":"1",
    "dmg":"5",
    "score":"0",
    "hp" :"25"
    }
player_stats["name"] = NameD
def spider():
    """spider Monster"""
    while True:
        spider={
            "hp":"10",
            "score":"20"
                }
        print("you are getting ambushed by giant spider !!!\n"
        + "what the hell do".title() +
        " you do ?".title() + "\nA.attack.\nB.run\nC.hide.".title())
        decide_1 = input("what do you do ? ".title()).title()
        if decide_1 == "A".upper():
            spider["hp"]=int(spider["hp"])-int(player_stats["dmg"])
            print("you did " + player_stats["dmg"] + " dmg to the spider")
            print("A.attack again\nB.try to pet him".title())
            decide_2 = input("now what ? ".title()).upper()
            if decide_2 == "A":
                spider["hp"]=int(spider["hp"])-int(player_stats["dmg"])
            elif decide_2 == "B":
                print("he got scared and ran away.".title())
                player_stats["score"] = int(player_stats["score"]) + int(spider["score"])
                print("you got "+spider["score"] + " points and now you have " +
                str(player_stats["score"]) + " points")
                break
            if spider["hp"]==0:
                print("you killed him !!".title())
                player_stats["score"] = int(player_stats["score"])+ int(spider["score"])
                print("you got "+spider["score"] + " points and now you have " +
                str(player_stats["score"]) + " points")
                break
        elif (decide_1=="B".upper()):
            print("you ran you coward.".title())
            break
        elif(decide_1=="C".upper()):
            print("you tried to hide.\nyou died.".title())
            break
spider()
print("you continue walking in the dungeon as ")
def troll(name):
    """A  Troll Encounter"""
    troll_stats = {
        "hp":"15",
        "score":"25",
        "dmg":"5"
        }
    while True:
        print(
            "a big troll comes out of nowhere and starts to shout in a gibbersh" +
            "\n what do you do ?".title()
            )
        print("A.attack the troll \nB.shout in gibbersh too")
        decide_3 = input("what shall you do " + name + " ?" )
        if (decide_3 == "a"):
            player_stats["hp"] = int(player_stats["hp"]) - int(troll_stats["dmg"])
            troll_stats["hp"] = int(troll_stats["hp"]) - int(player_stats["dmg"])
            print("you attacked the troll bu he attacked too, you've lost " +
                troll_stats["dmg"] + " hp and the troll lost" + player_stats["dmg"] +
                " hp and now has " + troll_stats["hp"] + "hp \n now what ?"
                )
            print("A.attack again \n B.Run")
            decide_4 = input("I'll ")
            if (decide_4 == "a"):
                print("as you try to attack again he just swings his great mace and kills you")
                break
            elif (decide_4 == "b"):
                print("you run and he's too slow to run so he shouts again and goes away")
                break
        elif (decide_3 == "B".title()):
            print("you shout in gibberish too causing the troll to cry and run")
            break
troll(player_stats["name"])
