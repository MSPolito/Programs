#One Gallon is 3.7854125 liters
gallons = float(input('Enter amount of gallons you wish to buy: '))
liters = 3.7854125 #Conversion rate of 1 gallon in liters
gallons_to_liters = gallons / liters
price_of_liters = gallons_to_liters * 0.88 #0.83 is the price in USD of 1 liter of Petrol
print('The price in USD per liter is: ', price_of_liters)
