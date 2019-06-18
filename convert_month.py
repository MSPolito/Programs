MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
old_date = input('Enter date in MM/DD/YYYY format: ')
month = old_date[0:2]
monthnme = MONTHS[int(month)-1]
print(monthnme,old_date[3:5],',', old_date[6:10])
