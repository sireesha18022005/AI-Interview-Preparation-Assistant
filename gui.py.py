import tkinter as tk
from tkinter import messagebox

questions = {
    "Software Engineer": [
        "What is OOP?",
        "What is Inheritance?",
        "What is a Database?"
    ],
    "Data Analyst": [
        "What is SQL?",
        "What is a Primary Key?",
        "What is Power BI?"
    ]
}

current_question = 0
score = 0

def start_interview():
    global current_question, score

    name = name_entry.get()
    role = role_var.get()

    if name == "":
        messagebox.showerror("Error", "Enter your name")
        return

    if role not in questions:
        messagebox.showerror("Error", "Select a role")
        return

    current_question = 0
    score = 0

    score_label.config(text="Score: 0")

    question_label.config(
        text=questions[role][current_question]
    )

def submit_answer():
    global current_question, score

    role = role_var.get()
    answer = answer_entry.get()

    if len(answer) > 20:
        score += 10
    elif len(answer) > 10:
        score += 5
    else:
        score += 2

    score_label.config(text=f"Score: {score}")

    answer_entry.delete(0, tk.END)

    current_question += 1

    if current_question < len(questions[role]):
        question_label.config(
            text=questions[role][current_question]
        )
    else:
        name = name_entry.get()

        messagebox.showinfo(
            "Interview Complete",
            f"Candidate: {name}\nFinal Score: {score}"
        )

        question_label.config(
            text="Interview Finished"
        )

root = tk.Tk()
root.title("AI Interview Assistant")
root.geometry("600x400")

title = tk.Label(
    root,
    text="AI Interview Assistant",
    font=("Arial", 18)
)
title.pack(pady=10)

tk.Label(root, text="Candidate Name").pack()

name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Select Role").pack()

role_var = tk.StringVar()

role_menu = tk.OptionMenu(
    root,
    role_var,
    "Software Engineer",
    "Data Analyst"
)
role_menu.pack()

start_btn = tk.Button(
    root,
    text="Start Interview",
    command=start_interview
)
start_btn.pack(pady=10)

question_label = tk.Label(
    root,
    text="Question will appear here",
    wraplength=500,
    font=("Arial", 12)
)
question_label.pack(pady=20)

answer_entry = tk.Entry(
    root,
    width=50
)
answer_entry.pack()

submit_btn = tk.Button(
    root,
    text="Submit Answer",
    command=submit_answer
)
submit_btn.pack(pady=10)

score_label = tk.Label(
    root,
    text="Score: 0",
    font=("Arial", 12)
)
score_label.pack()

root.mainloop()