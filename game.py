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
bet = None
wager = 0
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

def pick_side(player_choice):
        player_choice = input("What number do you bet on?: ")
        while player_choice.isdigit() == False:
                print("That is not a number.")
                player_choice = input("Pick side 1-6: ")
        while not player_choice == "1" and not player_choice == "2" and not player_choice == "3" and not player_choice == "4" and not player_choice == "5" and not player_choice == "6":
                print("That is not an option.")
                player_choice = input("Pick 1-6 please: ")
        return player_choice
def select_again(selection):
        while selection.isdigit() == False:
               print("That is not a number.")
               selection = input("Pick 2 or 3: ")
        while not selection == "2" and not selection == "3":
            print("That is not an option.")
            selection = input("Pick 2 or 3: ")
        return selection
def gambling(waging, money):
    while True:
        waging = input("Place wager: ")
        try:
            val = int(waging)
            if val <= money and val > 0:
                break
            else:
                print("Value invalid")
        except ValueError:
            print("Your wager must be an interger.")
        return waging

while running:
    print(cash)
    dealing()
    pick_side(bet)
    gambling(wager, cash)
    amount_of_dice = input("How many dice would you like to roll?: ")
    amount_of_dice = select_again(amount_of_dice)
    amount_of_dice = int(amount_of_dice)
    player_roll(amount_of_dice)
