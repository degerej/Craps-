# Joe Degere
# October 23rd 2019
# Craps!


import random


def balance():
    print("ENTER bankroll:")
    return int(input("> "))


bigbank = balance()


print(f"Enter the amount you want to bet from your bank {bigbank}")
bet = int(input("> "))


while bet <= bigbank:
    roll = random.randint(2,12)

    print(f"You rolled a {roll}")

    if roll == 7 or roll == 11:
        print("You win!")
        bank = bigbank + bet
        print(f"You now have {bank} in your bank.")

    elif roll == 2 or roll == 3 or roll == 12:
        print("You lose!")
        bank = bigbank - bet
        print(f"Now you have {bigbank} in your bank.")
    else:
        print("This value becomes your point, you must roll this value again to win, or roll a 7 and lose!")
        point = roll

        roll = random.randint(2,12)

        while roll != point and roll != 7:
            print(f"You have rolled a {roll}, roll again.")
            roll = random.randint(2,12)

        if roll == point:
            bank = bigbank + bet
            print("You win! You rolled point!")
            print(f"You now have {bank} in your bank!")
        else:
            bank = bigbank - bet
            print("You rolled a 7, You Lose!")
    print("If you would like to play again? yes or no")
    choice = input()
    if choice == "yes":
        print(f"You have {bigbank} in your bank. How much would you like to bet?")
        bet = int(input("> "))
        if bet > bigbank:
            print(f"You can't bet more than what you have in your bank. The game will now end.")
            bigbank = 0
    else:
        bigbank = 0

while bet <= 0:
    print("Invalid input, try again")
    bet = int(input("> "))
