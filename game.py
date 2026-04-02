#Dice roller program.
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
forced_bet = 0
dice_rolled_one = 0
dice_rolled_two = 0
dice_rolled_three = 0
dice_rolled_four = 0
dice_rolled_five = 0
dice_rolled_six = 0
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
        while not selection == "2"  and not selection == "3":
                print("That is not an option.")
                selection = input("Pick 2 or 3: ")
        return selection
def gambling(waging, money):
        while True:
                waging = input("Enter your wager: ")
                try:
                                val = int(waging)
                                if val <= money and val > 0:
                                        break
                                else:
                                        print("Value Invalid.")
                except ValueError:
                        print("Your wager must be an interger.")

        
        return waging
def winner(dice ,given_bet):
        win_multiplier = 0
        if dice.count(given_bet) >= 2:
                win_multiplier += dice.count(given_bet)
        else:
                print("You lose. ):")
        return win_multiplier
        
roll_cost = 0

while True:
        print("You need a minimum of $10,000 to win.")
        while running:
                player_side = None
                player_wager = 0
                amount_player_wins = 0
                dice.clear()
                print(f"Cash: ${cash}")
                dealing()
                if forced_bet > 0:
                        print(f"You were forced to bet ${forced_bet}")
                print(f"1:{dice_rolled_one}/ 2:{dice_rolled_two}/ 3:{dice_rolled_three}/ 4:{dice_rolled_four}/ 5:{dice_rolled_five}/ 6:{dice_rolled_six}")    
                player_side = int(pick_side(bet))
                player_wager = int(gambling(wager, cash))
                print(player_side)
                cash -= player_wager
                cash -= forced_bet
                print(f"Cash: ${cash}")
                print(f"Your cost to roll is: ${roll_cost}")
                amount_of_dice = input("How many dice would you like to roll?: ")
                amount_of_dice = select_again(amount_of_dice)
                amount_of_dice = int(amount_of_dice)
                player_roll(amount_of_dice)
                cash -= roll_cost
                if amount_of_dice == 2:
                        roll_cost += random.randint(25, 50)
                elif amount_of_dice == 3:
                        roll_cost += random.randint(50, 100)
                amount_player_wins = winner(dice, player_side)
                if amount_player_wins >= 2:
                        cash += (player_wager + forced_bet) * amount_player_wins
                forced_bet += 10
                dice_rolled_one += dice.count(1)
                dice_rolled_two += dice.count(2)
                dice_rolled_three += dice.count(3)
                dice_rolled_four += dice.count(4)
                dice_rolled_five += dice.count(5)
                dice_rolled_six += dice.count(6)

                if cash >= 10000:
                        end_game = input("Would you like to continue?: ").capitalize()
                        if end_game == "No":
                         print("Congrats!!!")
                         running = False
                if cash <= 0:
                        print("Game Over")
                        running = False 

        print("Final Score")
        print("-----------")
        print(f"Cash: {cash}")
        restart = input("Restart(Y/N): ").capitalize()
        if restart == "Y":
                cash = 1000
                forced_bet = 0
                dice_rolled_one = 0
                dice_rolled_two = 0
                dice_rolled_three = 0
                dice_rolled_four = 0
                dice_rolled_five = 0
                dice_rolled_six = 0
                roll_cost = 0
                running = True
        else:
                break
