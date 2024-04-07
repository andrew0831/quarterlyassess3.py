import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# Connect to the database (create if not exists)
conn = sqlite3.connect('quiz_database.db')
cursor = conn.cursor()

# Create a table to store quiz categories
cursor.execute('''CREATE TABLE IF NOT EXISTS Categories (
                    CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT NOT NULL
                    )''')

# Create a table to store quiz questions
cursor.execute('''CREATE TABLE IF NOT EXISTS Questions (
                    QuestionID INTEGER PRIMARY KEY AUTOINCREMENT,
                    CategoryID INTEGER NOT NULL,
                    QuestionText TEXT NOT NULL,
                    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
                    )''')

# Create a table to store options for each question
cursor.execute('''CREATE TABLE IF NOT EXISTS Options (
                    OptionID INTEGER PRIMARY KEY AUTOINCREMENT,
                    QuestionID INTEGER NOT NULL,
                    OptionText TEXT NOT NULL,
                    IsCorrect INTEGER NOT NULL DEFAULT 0,
                    FOREIGN KEY (QuestionID) REFERENCES Questions(QuestionID)
                    )''')

# Create a table to store user responses
cursor.execute('''CREATE TABLE IF NOT EXISTS UserResponses (
                    ResponseID INTEGER PRIMARY KEY AUTOINCREMENT,
                    QuestionID INTEGER NOT NULL,
                    SelectedOptionID INTEGER NOT NULL,
                    FOREIGN KEY (QuestionID) REFERENCES Questions(QuestionID),
                    FOREIGN KEY (SelectedOptionID) REFERENCES Options(OptionID)
                    )''')

# Commit the changes and close the connection
conn.commit()
conn.close()


QUESTIONS = {
    "Literature": [
        {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["Harper Lee", "J.D. Salinger", "Ernest Hemingway", "Mark Twain"], "answer": "Harper Lee"},
        {"question": "Which novel is James Joyce best known for?", "options": ["Ulysses", "Finnegans Wake", "A Portrait of the Artist as a Young Man", "The Dubliners"], "answer": "Ulysses"},
        {"question": "What is the main theme of 'Moby Dick'?", "options": ["Revenge", "Love", "Friendship", "War"], "answer": "Revenge"},
        {"question": "Who wrote 'One Hundred Years of Solitude'?", "options": ["Gabriel Garcia Marquez", "Mario Vargas Llosa", "Julio Cortázar", "Jorge Luis Borges"], "answer": "Gabriel Garcia Marquez"},
        {"question": "What is iambic pentameter?", "options": ["A type of poem", "A rhyme scheme", "A meter in poetry", "A figure of speech"], "answer": "A meter in poetry"},
        {"question": "Which of these is a famous play by Shakespeare?", "options": ["Hamlet", "Utopia", "Inferno", "Les Misérables"], "answer": "Hamlet"},
        {"question": "Who is the author of 'Pride and Prejudice'?", "options": ["Emily Brontë", "Charlotte Brontë", "Jane Austen", "Louisa May Alcott"], "answer": "Jane Austen"},
        {"question": "What genre is '1984' by George Orwell?", "options": ["Romance", "Dystopian", "Comedy", "Historical Fiction"], "answer": "Dystopian"},
        {"question": "Who wrote 'The Great Gatsby'?", "options": ["F. Scott Fitzgerald", "Ernest Hemingway", "William Faulkner", "John Steinbeck"], "answer": "F. Scott Fitzgerald"},
        {"question": "What is 'The Divine Comedy'?", "options": ["A play", "A poem", "A novel", "A short story"], "answer": "A poem"},
    ],
    "Programming": [
        {"question": "What does 'OOP' stand for?", "options": ["Object-Oriented Programming", "Objective Oriented Programming", "Optimal Operation Processing", "None of the above"], "answer": "Object-Oriented Programming"},
        {"question": "Which language is primarily used for Android App Development?", "options": ["Swift", "Kotlin", "Ruby", "C#"], "answer": "Kotlin"},
        {"question": "What is a 'fork' in the context of software development?", "options": ["A code branching strategy", "A tool for eating", "A version control strategy", "A hardware device"], "answer": "A version control strategy"},
        {"question": "What is recursion?", "options": ["A type of loop", "A function calling itself", "A debugging technique", "An error"], "answer": "A function calling itself"},
        {"question": "What does 'SQL' stand for?", "options": ["Structured Question Language", "Structured Query Language", "Simple Query Language", "None of the above"], "answer": "Structured Query Language"},
        {"question": "Which of these is not a Python data type?", "options": ["list", "tuple", "array", "dictionary"], "answer": "array"},
        {"question": "What is GitHub?", "options": ["A programming language", "A code editor", "A version control platform", "A database management system"], "answer": "A version control platform"},
        {"question": "Which of these is a JavaScript framework?", "options": ["Django", "Laravel", "Angular", "Flask"], "answer": "Angular"},
        {"question": "What is 'machine learning'?", "options": ["A type of computer", "A data analysis method", "A programming paradigm", "An AI that creates machines"], "answer": "A data analysis method"},
        {"question": "What is 'Agile'?", "options": ["A programming language", "A database system", "A project management methodology", "A type of software"], "answer": "A project management methodology"},
    ],
    "Database": [
        {"question": "What does 'ACID' stand for in databases?", "options": ["Atomicity, Consistency, Isolation, Durability", "Atomicity, Concurrency, Isolation, Durability", "Atomicity, Consistency, Integrity, Durability", "None of the above"], "answer": "Atomicity, Consistency, Isolation, Durability"},
        {"question": "Which SQL statement is used to extract data from a database?", "options": ["GET", "EXTRACT", "SELECT", "PULL"], "answer": "SELECT"},
        {"question": "What is a 'primary key'?", "options": ["A unique key for each row in a table", "A main keyboard key", "A master key for database encryption", "None of the above"], "answer": "A unique key for each row in a table"},
        {"question": "What is 'normalization'?", "options": ["Making the database normal", "Optimizing the database structure", "Reducing data redundancy and improving data integrity", "Increasing database size"], "answer": "Reducing data redundancy and improving data integrity"},
        {"question": "What does 'NoSQL' stand for?", "options": ["Not Only SQL", "No SQL allowed", "Not SQL", "None of the above"], "answer": "Not Only SQL"},
        {"question": "What is a 'document store'?", "options": ["A NoSQL database that stores data in JSON, BSON, or XML documents", "A place to store physical documents", "A feature in SQL databases", "None of the above"], "answer": "A NoSQL database that stores data in JSON, BSON, or XML documents"},
        {"question": "What is 'data mining'?", "options": ["Extracting valuable information from a database", "Mining for digital currency", "Removing data from a database", "Storing data in a mine"], "answer": "Extracting valuable information from a database"},
        {"question": "What is a 'relational database'?", "options": ["A database structured to recognize relations among stored items of information", "A database that is related to another database", "A social media database for relationships", "None of the above"], "answer": "A database structured to recognize relations among stored items of information"},
        {"question": "What is 'benchmarking'?", "options": ["A process where a company compares its performance with that of other companies to find ways to improve its own processes and practices", "Setting the highest standards for products", "A financial metric used to assess the profitability of a business", "A method of measuring employee performance"], "answer": "A process where a company compares its performance with that of other companies to find ways to improve its own processes and practices"}

    ],
    "Statistics": [
        {"question": "What is the median of the data set 3, 7, 9, 5, 12?", "options": ["7", "6.2", "9", "5"], "answer": "7"},
        {"question": "What does the 'standard deviation' measure?", "options": ["Average deviation from the mean", "Total variation within a data set", "The spread of a data set", "The middle value of a data set"], "answer": "The spread of a data set"},
        {"question": "What is a 'null hypothesis'?", "options": ["A statement that indicates no effect or no difference", "A statement to be proved null", "A hypothesis that is unlikely to be true", "A hypothesis that has been disproven"], "answer": "A statement that indicates no effect or no difference"},
        {"question": "Which test would you use to compare the means of two independent samples?", "options": ["Chi-square test", "ANOVA", "T-test", "Correlation coefficient"], "answer": "T-test"},
        {"question": "What is 'regression analysis' used for?", "options": ["To classify data into different categories", "To describe the association between variables", "To predict the value of a dependent variable based on the value of at least one independent variable", "To compute the mean of a data set"], "answer": "To predict the value of a dependent variable based on the value of at least one independent variable"},
        {"question": "What does 'P-value' in hypothesis testing indicate?", "options": ["The probability of correctly rejecting the null hypothesis", "The probability of observing the data, or something more extreme, if the null hypothesis is true", "The likelihood that the test statistic is at least as extreme as the observed value", "The proportion of the data that supports the alternative hypothesis"], "answer": "The probability of observing the data, or something more extreme, if the null hypothesis is true"},
        {"question": "What is 'Bayesian statistics'?", "options": ["A statistical method that applies probability to statistical problems", "A technique for creating statistical models", "A method for testing hypotheses", "A rule for decision making under uncertainty"], "answer": "A statistical method that applies probability to statistical problems"},
        {"question": "What is the mode of the data set 4, 8, 2, 8, 12, 8, 3?", "options": ["8", "7", "4", "3"], "answer": "8"},
        {"question": "What is a 'confidence interval'?", "options": ["A range of values within which the true population parameter is expected to lie, with a certain level of confidence", "A method for testing whether a statement about a population parameter is correct", "A set of values used for hypothesis testing", "The interval within which the majority of data points in a distribution fall"], "answer": "A range of values within which the true population parameter is expected to lie, with a certain level of confidence"},
        {"question": "What is 'correlation'?", "options": ["A measure of the relationship between two variables", "The average value of a data set", "A statistical measure that indicates the extent to which two or more variables fluctuate together", "A and C"], "answer": "A and C"},
    ],
    "Business Management": [
        {"question": "What is 'SWOT analysis'?", "options": ["Analysis of Strengths, Weaknesses, Opportunities, and Threats", "A method for determining market position", "A financial analysis technique", "A productivity measurement tool"], "answer": "Analysis of Strengths, Weaknesses, Opportunities, and Threats"},
        {"question": "What is the primary goal of 'supply chain management'?", "options": ["To minimize the cost of supplies", "To speed up production", "To ensure the timely delivery and quality of resources needed to produce products", "To create a chain of supplies"], "answer": "To ensure the timely delivery and quality of resources needed to produce products"},
        {"question": "What does 'corporate social responsibility' (CSR) refer to?", "options": ["A company's commitment to manage the social, environmental, and economic effects of its operations responsibly", "The responsibility of a corporation to increase its profits", "A legal obligation for corporations to act in the interest of their shareholders", "The social responsibility of businesses to avoid paying taxes"], "answer": "A company's commitment to manage the social, environmental, and economic effects of its operations responsibly"},
        {"question": "What is 'lean manufacturing'?", "options": ["A manufacturing process that looks to gain 'more for less' by reducing waste", "A method of manufacturing that focuses on high-quality production", "A traditional method of manufacturing that prioritizes quantity over quality", "A process that requires significant investment in raw materials"], "answer": "A manufacturing process that looks to gain 'more for less' by reducing waste"},
        {"question": "What is 'market segmentation'?", "options": ["The process of dividing a broad consumer or business market, normally consisting of existing and potential customers, into sub-groups of consumers based on some type of shared characteristics", "A marketing strategy that involves selling the same product to all consumers", "The act of increasing market share through aggressive sales techniques", "The division of a market into different geographical areas"], "answer": "The process of dividing a broad consumer or business market, normally consisting of existing and potential customers, into sub-groups of consumers based on some type of shared characteristics"},
        {"question": "What is the main purpose of 'strategic planning' in business?", "options": ["To set long-term objectives and identify the strategies to achieve them", "To deal with day-to-day operational issues", "To forecast future financial performance", "To analyze the past performance of the company"], "answer": "To set long-term objectives and identify the strategies to achieve them"},
        {"question": "What is 'brand equity'?", "options": ["The total value of a company's assets", "The differential impact that knowing the brand name has on customer response to the product or its marketing", "The amount of money a brand spends on marketing", "The equity shareholders have in a business"], "answer": "The differential impact that knowing the brand name has on customer response to the product or its marketing"},
        {"question": "What does 'B2B' stand for?", "options": ["Business to Business", "Back to Basics", "Business to Board", "Business to Bank"], "answer": "Business to Business"},
        {"question": "What is 'benchmarking'?", "options": ["A process where a company compares its performance with that of other companies to find ways to improve its own processes and practices", "Setting the highest standards for products", "A financial metric used to assess the profitability of a business", "A method of measuring employee performance"], "answer": "A process where a company compares its performance with that of other companies to find ways to improve its own processes and practices"}
    ],
}

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

