import random

def play_slot_machine(symbols = ['sevens', 'oranges', 'lemons','cash','gold bar', 'cherries','WIN', 'grapes'], wheels = 3):
    roulette = random.sample(symbols, 3)
    return(roulette)
play_slot_machine()
