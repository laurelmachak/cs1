'''Build a working roulette game.  At minimum, this script should
Complete one round of roulette - but if you're up to the challenge,
feel free to build a full command line interface through which '''

''' using rules of american roulette bc contains boty 0 (0) and 00 (37) '''

import random
random.seed(1)

bank_account = 1000
bet_amount = 0
bet_color = None
bet_number = None

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

def take_bet(color, number, amount):
    ''' probably don't need to take
    arguments but works with logic of play_game
    function right now.
     '''

     ''' this function returns array of the players
     color, number, and bet amount 
      '''
    global bank_account
    valid_colors = ["black", "green", "red"]
    while color not in valid_colors:
        color = input("choose color to bet on (green, black, or red): ")
    while (number == None) or not(0 <= number <= 37):
        number = int(input("choose a number to bet on (0-37): "))
    while not(0 < amount < bank_account):
        amount = int(input("how much money to bet?: "))
    return [color, number, amount]

def roll_ball():
    '''returns a random number between 0 and 37'''
    result = random.randint(0,37)
    return result


def check_results(result, color, number):
    '''Compares bet_color to color rolled.  Compares
    bet_number to number_rolled.'''
    ''' takes the result of roll_ball(), and
    the users bet color & number as inputs  '''

    #check what array the rolled num is in
    if result in green:
        result_color = "green"
    elif result in red:
        result_color = "red"
    elif result in black:
        result_color = "black"

    #comparing rollers
    if result_color == color:
        color_check = True
    else:
        color_check = False
    if result == number:
        num_check = True
    else:
        num_check = False
    return [color_check, num_check, result_color]



def payout(color_check, num_check, bet):
    '''returns total amount won or lost by user based on results of roll. '''
    if color_check and num_check:
        winnings = bet
    elif color_check or num_check:
        winnings = bet/2
    else:
        winnings = bet*(-1)
    return winnings


def play_game():
    """This is the main function for the game.
    When this function is called, one full iteration of roulette,
    including:
    Take the user's bet.
    Roll the ball.
    Determine if the user won or lost.
    Pay or deduct money from the user accordingly.
    """
    global bet_color
    global bet_number
    global bet_amount
    print("\nWelcome to the mini & fake roulette!\n")
    bet = take_bet(bet_color, bet_number, bet_amount)
    bet_color = bet[0]
    bet_number = bet[1]
    bet_amount = bet[2]
    print("bet color:",bet_color)
    print("number bet on:",bet_number)
    print("money bet:", bet_amount)

    print("\nrolling ball...\n")
    result = roll_ball()
    print("ball landed on number:", result)
    player_outcome = check_results(result, bet_color, bet_number)
    print("ball landed on color:", player_outcome[2])
    color_check = player_outcome[0]
    num_check = player_outcome[1]

    money_in_or_out = payout(color_check, num_check, bet_amount)
    print("\nmoney won or lost:", money_in_or_out)
    global bank_account
    print("bank account before:", bank_account)
    bank_account += money_in_or_out
    print("bank account after:", bank_account)

    #return money_in_or_out

play_game()
