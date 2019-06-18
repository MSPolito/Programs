import random
from Project_2 import *

spin = play_slot_machine()
play_slot_machine()
gamble_sim()

#Bullet points 1-2
result = calc_prize_five(spin)
if result != "LOSE":
    print("You won " + result + "!")
else:
    print("You lost")
    
#Bullet points 3
print(gamble_sim())
