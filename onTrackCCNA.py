import datetime
import tkinter as tk

#need to add a way to enter what day of content you are on 

def calculate_plan():
    today = datetime.date.today()
    year = int(year_entry.get())
    month = int(month_entry.get())
    day = int(day_entry.get())
    future = datetime.date(year, month, day)
    diff = future - today
    weeks = diff.days / 7
    program = int(program_entry.get())
    cday = int(cday_entry.get())

    if program == 1:
        cday = int(cday_entry.get())
        daysLeft = 63 - cday
        contentBudget = round((daysLeft / weeks),2)
        dailyGoal = round((contentBudget / 7),2)
        dailyGoalWork = round((contentBudget / 5),2)
        result_label.config(text="This week you should get {} days/sections of content done meaning:\n\n{} days of content a day on a 7 day track\n\n{} days of content on a 5 day track".format(contentBudget, dailyGoal, dailyGoalWork))
    elif program == 2:
        cday = int(cday_entry.get())
        daysLeft = 39 - cday
        contentBudget = round((daysLeft / weeks),2)
        dailyGoal = round((contentBudget / 7),2)
        dailyGoalWork = round((contentBudget / 5),2)
        result_label.config(text="This week you should get {} days/sections of content done meaning:\n\n{} days of content a day on a 7 day track\n\n{} days of content on a 5 day track".format(contentBudget, dailyGoal, dailyGoalWork))
    else:
        result_label.config(text="Invalid input")

root = tk.Tk()
root.title("CCNA Planner")

year_label = tk.Label(root, text="Enter your test year:")
year_label.pack()

year_entry = tk.Entry(root)
year_entry.pack()

month_label = tk.Label(root, text="Enter your test month:")
month_label.pack()

month_entry = tk.Entry(root)
month_entry.pack()

day_label = tk.Label(root, text="Enter your test day:")
day_label.pack()

day_entry = tk.Entry(root)
day_entry.pack()

program_label = tk.Label(root, text="Type 1 for Jeremy's IT Lab and 2 for Flack Box")
program_label.pack()

program_entry = tk.Entry(root)
program_entry.pack()

cday_label = tk.Label(root, text="Enter the day/section you are on")
cday_label.pack()

cday_entry = tk.Entry(root)
cday_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_plan)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()


