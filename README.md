# QuizBowl GUI

## Files
1. quizbowl.py: This script connects to an SQLite database (quiz_database.db), populates it using an SQL        script (populate.sql), and retrieves quiz questions categorized by topic from the database. It then          presents these questions in a graphical user interface using Tkinter, allowing users to select a quiz        category, answer multiple-choice questions, and view their score upon completion.
  
2. populate.sql: This SQL script creates two tables: `Categories` and `class Questions`, and populates          them with data. The `Categories` table stores unique quiz categories, while the `class Questions` table      stores individual questions along with their respective options and correct answers, categorized by the      `CategoryName` field. Additionally, it inserts data into these tables for categories such as                 Literature, Programming, Database, Statistics, and Business Management, along with corresponding             questions and answers.
  
3. quiz_database.db:This file gets populated with the queries from populate.sql and is used by the app to quiz users.

## How to run
1. After running the script, a GUI window should appear with a dropdown menu listing the available quiz categories.

2. Select a category from the dropdown menu and click the "Start Quiz Now" button.
   
3. The quiz questions related to the selected category will be displayed one by one.

4. Choose the correct answer for each question by selecting the corresponding radio button.

5. Click the "Next" button to proceed to the next question.

6. After answering all questions, a message box will display your quiz completion status along with your score.

7. Close the GUI window to exit the application.
