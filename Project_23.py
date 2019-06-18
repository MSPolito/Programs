from Project_22 import *
from Project_21 import *
def gamble_sim(capital = int(input('How much money do you have?: ')) , bet_amount = int(input('How much do you want to bet?: ')), max_plays = 10000):
    counter = 0
    while(capital > 0 or counter < max_plays):
        capital += bet_amount
        counter += 1
        prize = calc_prize_five(play_slot_machine())
    if prize == 'Lose':
        capital = bet_amount * prize
        return capital
gamble_sim()
