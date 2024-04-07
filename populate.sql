-- Create a table to store quiz categories
CREATE TABLE IF NOT EXISTS Categories (
    CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL
);

-- Create a table to store quiz questions
CREATE TABLE IF NOT EXISTS Questions (
    QuestionID INTEGER PRIMARY KEY AUTOINCREMENT,
    CategoryID INTEGER NOT NULL,
    QuestionText TEXT NOT NULL,
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);

-- Create a table to store options for each question
CREATE TABLE IF NOT EXISTS Options (
    OptionID INTEGER PRIMARY KEY AUTOINCREMENT,
    QuestionID INTEGER NOT NULL,
    OptionText TEXT NOT NULL,
    IsCorrect INTEGER NOT NULL DEFAULT 0, -- 1 if option is correct, 0 otherwise
    FOREIGN KEY (QuestionID) REFERENCES Questions(QuestionID)
);

-- Create a table to store user responses
CREATE TABLE IF NOT EXISTS UserResponses (
    ResponseID INTEGER PRIMARY KEY AUTOINCREMENT,
    QuestionID INTEGER NOT NULL,
    SelectedOptionID INTEGER NOT NULL,
    FOREIGN KEY (QuestionID) REFERENCES Questions(QuestionID),
    FOREIGN KEY (SelectedOptionID) REFERENCES Options(OptionID)
);

-- Insert literature questions
INSERT INTO Questions (CategoryID, QuestionText, Answer)
VALUES
    (1, 'Who wrote ''To Kill a Mockingbird''?', 'Harper Lee'),
    (1, 'Which novel is James Joyce best known for?', 'Ulysses'),
    (1, 'What is the main theme of ''Moby Dick''?', 'Revenge'),
    (1, 'Who wrote ''One Hundred Years of Solitude''?', 'Gabriel Garcia Marquez'),
    (1, 'What is iambic pentameter?', 'A meter in poetry'),
    (1, 'Which of these is a famous play by Shakespeare?', 'Hamlet'),
    (1, 'Who is the author of ''Pride and Prejudice''?', 'Jane Austen'),
    (1, 'What genre is ''1984'' by George Orwell?', 'Dystopian'),
    (1, 'Who wrote ''The Great Gatsby''?', 'F. Scott Fitzgerald'),
    (1, 'What is ''The Divine Comedy''?', 'A poem');

-- Insert programming questions
INSERT INTO Questions (CategoryID, QuestionText, Answer)
VALUES
    (2, 'What does ''OOP'' stand for?', 'Object-Oriented Programming'),
    (2, 'Which language is primarily used for Android App Development?', 'Kotlin'),
    (2, 'What is a ''fork'' in the context of software development?', 'A version control strategy'),
    (2, 'What is recursion?', 'A function calling itself'),
    (2, 'What does ''SQL'' stand for?', 'Structured Query Language'),
    (2, 'Which of these is not a Python data type?', 'array'),
    (2, 'What is GitHub?', 'A version control platform'),
    (2, 'Which of these is a JavaScript framework?', 'Angular'),
    (2, 'What is ''machine learning''?', 'A data analysis method'),
    (2, 'What is ''Agile''?', 'A project management methodology');

-- Insert database questions
INSERT INTO Questions (CategoryID, QuestionText, Answer)
VALUES
    (3, 'What does ''ACID'' stand for in databases?', 'Atomicity, Consistency, Isolation, Durability'),
    (3, 'Which SQL statement is used to extract data from a database?', 'SELECT'),
    (3, 'What is a ''primary key''?', 'A unique key for each row in a table'),
    (3, 'What is ''normalization''?', 'Reducing data redundancy and improving data integrity'),
    (3, 'What does ''NoSQL'' stand for?', 'Not Only SQL'),
    (3, 'What is a ''document store''?', 'A NoSQL database that stores data in JSON, BSON, or XML documents'),
    (3, 'What is ''data mining''?', 'Extracting valuable information from a database'),
    (3, 'What is a ''relational database''?', 'A database structured to recognize relations among stored items of information'),
    (3, 'What is ''benchmarking''?', 'A process where a company compares its performance with that of other companies to find ways to improve its own processes and practices');

-- Insert statistics questions
INSERT INTO Questions (CategoryID, QuestionText, Answer)
VALUES
    (4, 'What is the median of the data set 3, 7, 9, 5, 12?', '7'),
    (4, 'What does the ''standard deviation'' measure?', 'The spread of a data set'),
    (4, 'What is a ''null hypothesis''?', 'A statement that indicates no effect or no difference'),
    (4, 'Which test would you use to compare the means of two independent samples?', 'T-test'),
    (4, 'What is ''regression analysis'' used for?', 'To predict the value of a dependent variable based on the value of at least one independent variable'),
    (4, 'What does ''P-value'' in hypothesis testing indicate?', 'The probability of observing the data, or something more extreme, if the null hypothesis is true'),
    (4, 'What is ''Bayesian statistics''?', 'A statistical method that applies probability to statistical problems'),
    (4, 'What is the mode of the data set 4, 8, 2, 8, 12, 8, 3?', '8'),
    (4, 'What is a ''confidence interval''?', 'A range of values within which the true population parameter is expected to lie, with a certain level of confidence'),
    (4, 'What is ''correlation''?', 'A measure of the relationship between two variables');

-- Insert business management questions
INSERT INTO Questions (CategoryID, QuestionText, Answer)
VALUES
    (5, 'What is ''SWOT analysis''?', 'Analysis of Strengths, Weaknesses, Opportunities, and Threats'),
    (5, 'What is the primary goal of ''supply chain management''?', 'To ensure the timely delivery and quality of resources needed to produce products'),
    (5, 'What does ''corporate social responsibility'' (CSR) refer to?', 'A company''s commitment to manage the social, environmental, and economic effects of its operations responsibly'),
    (5, 'What is ''lean manufacturing''?', 'A manufacturing process that looks to gain ''more for less'' by reducing waste'),
    (5, 'What is ''market segmentation''?', 'The process of dividing a broad consumer or business market, normally consisting of existing and potential customers, into sub-groups of consumers based on some type of shared characteristics'),
    (5, 'What is the main purpose of ''strategic planning'' in business?', 'To set long-term objectives and identify the strategies to achieve them'),
    (5, 'What is ''brand equity''?', 'The differential impact that knowing the brand name has on customer response to the product or its marketing'),
    (5, 'What does ''B2B'' stand for?', 'Business to Business'),
    (5, 'What is ''benchmarking''?', 'A process where a company compares its performance with that of other companies to find ways to improve its own processes and practices');

-- Users table
INSERT INTO Users (Username, Password)
VALUES
    ('user1', 'password1'),
    ('user2', 'password2'),
    ('user3', 'password3');

-- Categories table
INSERT INTO Categories (CategoryName)
VALUES
    ('Literature'),
    ('Programming'),
    ('Database'),
    ('Statistics'),
    ('Business Management');



