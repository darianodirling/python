import datetime

today = datetime.date.today()
future = datetime.date(2021,12,15)
diff = future - today
#print (diff.days)

weeks = diff.days / 7

print('how pirate meals do you have? ')
meals = int(input())

print('how many pirate bucks do you have left? ')
bucks = int(input())

MealBudget = round(meals / weeks)
BuckBudget = round(bucks / weeks)

print("This week you should use: " + str(MealBudget) + " meals" + " and " + str(BuckBudget) + " bucks")
input('Press ENTER to exit')