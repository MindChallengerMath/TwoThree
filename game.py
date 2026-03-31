import random
import math
#● ┌ ─ ┐ │ └ ┘

dice_art = {
    1: ("┌---------┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└---------┘")
, 2:   ("┌---------┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└---------┘")
, 3:   ("┌---------┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└---------┘")
,4:    ("┌---------┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└---------┘")
, 5:   ("┌---------┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└---------┘")
 ,6:   ("┌---------┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└---------┘")
}

running = True
dice = []
cash = 1000
def dealing():
        for dealer_die in range(random.randint(0,2)):
           dice.append(random.randint(1,6))
        for line in range(5):
                        for die in dice:
                                print(dice_art.get(die)[line], end="")
                        print()
def player_roll(amount_of_dice):
        if amount_of_dice == 2 or amount_of_dice == 3:
                for die in range(amount_of_dice):
                        dice.append(random.randint(1,6))
                for line in range(5):
                        for die in dice:
                                print(dice_art.get(die)[line], end="")
                        print()

def pick_side():
        choose_side = input("")
def select_again(selection):
        while selection.isdigit() == False:
               print("That is not a number.")
               selection = input("Pick 2 or 3: ")
        return selection


while running:
    print(cash)
    dealing()
    amount_of_dice = input("How many dice would you like to roll?: ")
    amount_of_dice = select_again(amount_of_dice)
    amount_of_dice = int(amount_of_dice)
    player_roll(amount_of_dice)
