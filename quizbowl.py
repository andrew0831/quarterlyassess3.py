import tkinter as tk
from tkinter import messagebox, ttk


QUESTIONS = {
    "Math": [
        {"question": "What is 2 + 2?", "options": ["1", "2", "3", "4"], "answer": "4"},
        {"question": "What is 5 x 5?", "options": ["10", "20", "25", "30"], "answer": "25"},
    ],
    "Science": [
        {"question": "Water freezes at 0 degrees on which temperature scale?", "options": ["Fahrenheit", "Celsius", "Kelvin", "Rankine"], "answer": "Celsius"},
        {"question": "What is the chemical symbol for Gold?", "options": ["Au", "Ag", "Pb", "Fe"], "answer": "Au"},
    ]
}

class QuestionFrame(tk.Frame):
    def __init__(self, master, questions, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.questions = questions
        self.current_question_index = 0
        self.display_current_question()
        self.pack()

    def display_current_question(self):
        question_data = self.questions[self.current_question_index]
        self.question = self.question(self, question_data["question"], question_data["options"], question_data["answer"], self.on_next)

    def on_next(self):
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.question.pack_forget()
            self.display_current_question()
        else:
            messagebox.showinfo("Quiz Completed", "You have completed the quiz!")
            self.master.destroy()

def start_quiz(category):
    quiz_window = tk.Tk()
    quiz_window.title(f"Quiz Bowl - {category}")
    QuestionFrame(quiz_window, QUESTIONS[category])
    quiz_window.mainloop()

def category_selection_window():
    window = tk.Tk()
    window.title("Quiz Bowl - Select Category")

    selected_category = tk.StringVar()
    category_dropdown = ttk.Combobox(window, textvariable=selected_category, values=list(QUESTIONS.keys()))
    category_dropdown.grid(column=0, row=0, padx=10, pady=10)

    start_button = tk.Button(window, text="Start Quiz Now", command=lambda: [window.destroy(), start_quiz(selected_category.get())])
    start_button.grid(column=0, row=1, padx=10, pady=10)

    window.mainloop()

category_selection_window()
