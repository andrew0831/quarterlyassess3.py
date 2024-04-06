import tkinter as tk
from tkinter import ttk

CATEGORIES = ["Math", "Science", "History", "Geography"]

def start_quiz(selected_category):
    print(f"Starting quiz for category: {selected_category}")

def category_selection_window():
    window = tk.Tk()
    window.title("Quiz Bowl - Select Category")

    selected_category = tk.StringVar()
    category_dropdown = ttk.Combobox(window, textvariable=selected_category, values=CATEGORIES)
    category_dropdown.grid(column=0, row=0, padx=10, pady=10)

    start_button = tk.Button(window, text="Start Quiz Now", command=lambda: start_quiz(selected_category.get()))
    start_button.grid(column=0, row=1, padx=10, pady=10)

    window.mainloop()

category_selection_window()

def open_quiz_window(category):
    quiz_window = tk.Tk()
    quiz_window.title(f"Quiz Bowl - {category}")

    questions = [
        {"question": "What is 2+2?", "options": ["2", "3", "4", "5"], "answer": "4"},
    ]

    def display_question(question):
        question_label = tk.Label(quiz_window, text=question["question"])
        question_label.pack()

        for option in question["options"]:
            option_button = tk.Radiobutton(quiz_window, text=option, value=option)
            option_button.pack()

    display_question(questions[0])  

    quiz_window.mainloop()

def start_quiz(selected_category):
    category_selection_window.destroy()  
    open_quiz_window(selected_category)  

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer

