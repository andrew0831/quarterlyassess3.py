import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

with open("quiz_database.db", "w") as file:
    pass

conn = sqlite3.connect('quiz_database.db')
cursor = conn.cursor()


with open("populate.sql", "r") as file:
    sql_script = file.read()
cursor.executescript(sql_script)
conn.commit()

QUESTIONS = {}
cursor.execute("SELECT * FROM Categories")
categories = cursor.fetchall()
for category in categories:
    category_id, category_name = category
    cursor.execute(f"SELECT * FROM Questions WHERE CategoryName = '{category_name}'")
    questions = cursor.fetchall()
    QUESTIONS[category_name] = []
    for question in questions:
        id, categoryName, question, options, answer = question
        question_dict = {
            "question": question,
            "options": options.split("\\n"), 
            "answer": answer
        }
        QUESTIONS[category_name].append(question_dict)
conn.close()

class Question:
    def __init__(self, master, question, options, answer, callback_on_next):
        self.master = master
        self.question = question
        self.options = options
        self.answer = answer
        self.callback_on_next = callback_on_next
        self.user_answer = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text=self.question).pack()
        for option in self.options:
            tk.Radiobutton(self.master, text=option, variable=self.user_answer, value=option).pack(anchor=tk.W)
        tk.Button(self.master, text="Next", command=self.on_next_click).pack()

    def on_next_click(self):
        is_correct = self.user_answer.get() == self.answer
        if is_correct:
            messagebox.showinfo("Correct", "That's Correct!")
        else:
            messagebox.showinfo("Incorrect", "That's Incorrect.")
        
        self.callback_on_next(is_correct)

class QuestionFrame(tk.Frame):
    def __init__(self, master, questions, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.questions = questions
        self.current_question_index = 0
        self.correct_answers = 0  
        self.display_current_question()
        self.pack()

    def display_current_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question = Question(self, question_data["question"], question_data["options"], question_data["answer"], self.on_answer)
        else:
            self.show_result()

    def on_answer(self, is_correct):
        if is_correct:
            self.correct_answers += 1  
        self.current_question_index += 1
        self.clear_widgets()
        self.display_current_question()

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"You have completed the quiz! Your score: {self.correct_answers}/{len(self.questions)}")
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

