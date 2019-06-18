def ratios(calories, carb = .4, protein = .3, fat = .3):
        return [round(carb*calories/4), round(protein*calories/4), round(fat*calories/9)]
print(ratios(0.3,0.3,2000))
