#The first three lines of this program are correct
#Be sure that you understand what the user inputs will look like
#They will only be in the formats specified including $ and % where indicated
item_cost = input('Enter cost of items: ') #input will include $ such as $42.50
ship_cost = input('Enter total shipping cost: ') #input will include $ such as $2.50
tax_rate = input('Enter tax percentage: ') #input will include % such as 5%
#Correct the last three lines
#Do not add extra lines, correct in place
tax_paid = (float(item_cost[1:]) + float(ship_cost[1:])) * (float(tax_rate[:-1])/100)
total_cost = float(item_cost[1:]) + tax_paid + float(ship_cost[1:])
print(tax_paid)
print(total_cost)
print('Total cost is, ' + str(total_cost))
