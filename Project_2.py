import random

def play_slot_machine(symbols = ['sevens', 'oranges', 'lemons','cash','gold bar','cherries','WIN', 'grapes',], wheels = 5):
    roulette = []
    for x in range(0, wheels):
         roulette += random.sample(symbols, 1)
    return roulette
play_slot_machine()

def calc_prize_five(selections):
    roulette = selections
    if selections[0] == selections[1] == selections[2] == selections[3] == selections[4] == 'WIN':
        return '50X'
    elif selections[0] == selections[1] == selections[2] == selections[3] == selections[4] != 'WIN':
        return '20X'
    elif selections[0] == selections[4] and selections[1] == selections[2] == selections[3]:
        return '15X'
    elif selections[0] == selections[2] == selections[4]:
        return '10X'
    elif selections[0] == selections[4]:
        return '5X'
    else:
        return 'LOSE'

# #Correct this function
# #You may not add or delete lines
# #You must correct lines in place, focus on indentation, logic, and correct usage of functions and variables

def gamble_sim(capital = 100 , bet_amount = 10, max_plays = 10000):
    counter = 0
    while (capital) > 0 and counter < max_plays:
        capital -= bet_amount
        counter += 1
        prize = calc_prize_five(play_slot_machine())
        if prize != 'LOSE':
            capital += bet_amount *int(prize[0:-1])
    return counter
#there should be no main program or test code in this file
#and especially NO INPUT LINES
