import random

def play_slot_machine(symbols = ['sevens', 'oranges', 'lemons','cash','gold bar', 'cherries','WIN', 'grapes'], wheels = 3):
	#fill in your function code and delete pass
	#if you submit for the checkpoint and you have not completed this function DO NOT delete pass
	pass 


def calc_prize_five(selections):
    #fill in your function code and delete pass
	#if you submit for the checkpoint and you have not completed this function DO NOT delete pass
    pass
	


#Correct this function
#You may not add or delete lines
#You must correct lines in place, focus on indentation, logic, and correct usage of functions and variables   
def gamble_sim(capital, bet_amount, max_plays = 10000):
	counter = 0
	while(capital > 0 or counter < max_plays):
		capital += bet_amount
		counter += 1
		prize = calc_prize_five(play_slot_machine())
		if prize not 'Lose':
			capital = bet_amount * prize
			return counter

#there should be no main program or test code in this file
#and especially NO INPUT LINES