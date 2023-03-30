#@author Darian O'Dirling
#This program helps you budget your meal plan

import tkinter as tk
import datetime

class PirateBudgetGUI:
    def __init__(self, master):
        self.master = master
        master.title("Pirate Budget")

        self.label1 = tk.Label(master, text="How many pirate meals do you have?")
        self.label1.pack()

        self.meals_entry = tk.Entry(master)
        self.meals_entry.pack()

        self.label2 = tk.Label(master, text="How many pirate bucks do you have left?")
        self.label2.pack()

        self.bucks_entry = tk.Entry(master)
        self.bucks_entry.pack()

        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate_budget)
        self.calculate_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.exit_button = tk.Button(master, text="Exit", command=master.quit)
        self.exit_button.pack()

    def calculate_budget(self):
        today = datetime.date.today()

        #Update this with the end of your semester
        future = datetime.date(2023, 5, 1)
        diff = future - today

        weeks = diff.days / 7

        meals = int(self.meals_entry.get())
        bucks = int(self.bucks_entry.get())

        meal_budget = round(meals / weeks)
        buck_budget = round(bucks / weeks)

        result = "This week you should use: {} meals and {} bucks".format(meal_budget, buck_budget)
        self.result_label.config(text=result)

# create the GUI
root = tk.Tk()
budget_gui = PirateBudgetGUI(root)
root.mainloop()
