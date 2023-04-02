import tkinter as tk
from tkinter import ttk

def calculate_grade():
    try:
        exam_score = float(exam_entry.get())
        attendance = float(attendance_entry.get())
        homework = float(homework_entry.get())

        final_grade = (exam_score * 0.67) + (attendance * 0.08) + (homework * 0.25)

        if final_grade >= 61:
            status = "Passing"
        else:
            status = "Not Passing"

        result_label.config(text=f"Your final grade is {final_grade:.2f}. You are {status}.")
        what_if_button.config(state="normal")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

def calculate_what_if():
    try:
        desired_grade = float(desired_grade_entry.get())
        current_exam_score = float(exam_entry.get())
        current_attendance = float(attendance_entry.get())
        current_homework = float(homework_entry.get())

        required_exam_score = (desired_grade - (current_attendance * 0.08) - (current_homework * 0.25)) / 0.67

        if 0 <= required_exam_score <= 100:
            what_if_result.config(text=f"To achieve a {desired_grade:.2f}, you need a {required_exam_score:.2f} on the next test.")
        else:
            what_if_result.config(text="The required score is out of range (0-100).")

    except ValueError:
        what_if_result.config(text="Invalid input. Please enter valid numbers.")

root = tk.Tk()
root.title("Grade Calculator")
root.geometry("370x370")

style = ttk.Style()
style.theme_use("clam")
style.configure(".", background="7393B3", foreground="#ffffff")
style.configure("TLabel", background="#7393B3", foreground="#ffffff")
style.configure("TButton", background="#7393B3", foreground="#ffffff")
style.configure("TEntry", fieldbackground="#ffffff", foreground="#000000")

title_label = ttk.Label(root, text="Okaay")
title_label.grid(row=0, column=0, columnspan=2, pady=(10, 5))

exam_label = ttk.Label(root, text="Exam Score (0-100):")
exam_label.grid(row=1, column=0, padx=(10, 5), pady=(5, 5), sticky="w")

exam_entry = ttk.Entry(root)
exam_entry.grid(row=1, column=1, padx=(5, 10), pady=(5, 5))

attendance_label = ttk.Label(root, text="Attendance (0-100):")
attendance_label.grid(row=2, column=0, padx=(10, 5), pady=(5, 5), sticky="w")

attendance_entry = ttk.Entry(root)
attendance_entry.grid(row=2, column=1, padx=(5, 10), pady=(5, 5))

homework_label = ttk.Label(root, text="Homework (0-100):")
homework_label.grid(row=3, column=0, padx=(10, 5), pady=(5, 5), sticky="w")

homework_entry = ttk.Entry(root)
homework_entry.grid(row=3, column=1, padx=(5, 10), pady=(5, 5))

calculate_button = ttk.Button(root,text="Calculate Grade", command=calculate_grade)
calculate_button.grid(row=4, column=0, columnspan=2, pady=(10, 5))

result_label = ttk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=(5, 10))

what_if_button = ttk.Button(root, text="Calculate What If?", command=calculate_what_if, state="disabled")
what_if_button.grid(row=6, column=0, columnspan=2, pady=(10, 5))

desired_grade_label = ttk.Label(root, text="Desired Final Grade (0-100):")
desired_grade_label.grid(row=7, column=0, padx=(10, 5), pady=(5, 5), sticky="w")

desired_grade_entry = ttk.Entry(root)
desired_grade_entry.grid(row=7, column=1, padx=(5, 10), pady=(5, 5))

what_if_result = ttk.Label(root, text="")
what_if_result.grid(row=8, column=0, columnspan=2, pady=(5, 10))

root.mainloop()
