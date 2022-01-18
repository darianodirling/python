import datetime

today = datetime.date.today()
future = datetime.date(2022,5,5)
diff = future - today
#print (diff.days)

weeks = diff.days / 7

print('How pirate meals do you have? ')
meals = int(input())

print('How many pirate bucks do you have left? ')
bucks = int(input())

MealBudget = round(meals / weeks)
BuckBudget = round(bucks / weeks)

print("This week you should use: " + str(MealBudget) + " meals" + " and " + str(BuckBudget) + " bucks")
print('Press ENTER to exit the program')
