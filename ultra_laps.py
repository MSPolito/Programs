distance = int(input('Enter ultra distance in miles: '))
laps = int(input('Enter length of laps in miles: '))
reclaps = int(distance / laps) #variable describes recommended laps
addmiles = float(distance % laps) #variable describes additionalmiles
print('You must run',reclaps, 'laps and', addmiles, 'additional miles')
