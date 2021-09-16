import datetime
 
today = datetime.date.today()
future = datetime.date(2021,11,30)
diff = future - today

if diff == 0:
    print ("HAPPY BIRTHDAY")
else:
    print ('Hello Darian there is '+ str(diff.days) + ' days till you are 21')

print ('press enter to close')
input('')
