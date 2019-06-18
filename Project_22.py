import random
from Project_21 import *
def calc_prize_five(selections):
    selections = [random.choice(symbols),random.choice(symbols), random.choice(symbols), random.choice(symbols), random.choice(symbols)]
    if (selections[0] == selections[1] == selections[2] == selections[3] == selections[4] == 'WIN'):
        return '50X'
    elif (selections[0] == selections[1]  == selections[2] == selections[3] == selections[4]):
        return '20X'
    elif (selections[0] == selections[4] and selections[1]  == selections[2] == selections[3]):
        return '15X'
    elif (selections[0] == selections[2] == selections[4]):
        return '10X'
    elif (selections[0] == selections[4]):
        return '5X'
    else:
        return('LOSE')
print(calc_prize_five())
	#if you submit for the checkpoint and you have not completed this function DO NOT delete pass
