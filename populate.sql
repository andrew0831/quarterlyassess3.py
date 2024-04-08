CREATE TABLE Categories (
    CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    CategoryName TEXT NOT NULL
);

INSERT INTO Categories (CategoryName) VALUES
    ('Literature'),
    ('Programming'),
    ('Database'),
    ('Statistics'),
    ('Business Management');

CREATE TABLE Questions (
    QuestionID INTEGER PRIMARY KEY AUTOINCREMENT,
    CategoryName TEXT NOT NULL,
    QuestionText TEXT NOT NULL,
    QuestionOptions TEXT NOT NULL,
    QuestionAnswers TEXT NOT NULL,
    FOREIGN KEY (CategoryName) REFERENCES Categories(CategoryName)
);

INSERT INTO Questions (CategoryName, QuestionText, QuestionOptions, QuestionAnswers) VALUES
('Literature', 'Who wrote "1984"?', 'George Orwell\nAldous Huxley\nRay Bradbury\nMargaret Atwood', 'George Orwell'),
('Literature', 'Who is the author of "Pride and Prejudice"?', 'Charlotte Brontë\nJane Austen\nEmily Brontë\nLouisa May Alcott', 'Jane Austen'),
('Literature', 'Which Shakespeare play features the characters Rosalind and Orlando?', 'As You Like It\nHamlet\nMacbeth\nThe Tempest', 'As You Like It'),
('Literature', 'What is the title of the first Harry Potter book?', 'Harry Potter and the Goblet of Fire\nHarry Potter and the Philosopher''s Stone\nHarry Potter and the Chamber of Secrets\nHarry Potter and the Prisoner of Azkaban', 'Harry Potter and the Philosopher''s Stone'),
('Literature', 'Who wrote "To Kill a Mockingbird"?', 'Harper Lee\nJ.D. Salinger\nErnest Hemingway\nMark Twain', 'Harper Lee'),
('Literature', 'Which novel begins with the line "Call me Ishmael."?', 'Moby-Dick\nThe Great Gatsby\n1984\nCatch-22', 'Moby-Dick'),
('Literature', 'In which century did Jane Austen live?', '16th Century\n17th Century\n18th Century\n19th Century', '19th Century'),
('Literature', 'Who created the character Sherlock Holmes?', 'Agatha Christie\nArthur Conan Doyle\nIan Fleming\nCharles Dickens', 'Arthur Conan Doyle'),
('Literature', 'What genre is the book "Brave New World" considered?', 'Science Fiction\nFantasy\nRomance\nHistorical Fiction', 'Science Fiction'),
('Literature', 'Who wrote "The Great Gatsby"?', 'F. Scott Fitzgerald\nErnest Hemingway\nJohn Steinbeck\nWilliam Faulkner', 'F. Scott Fitzgerald');

INSERT INTO Questions (CategoryName, QuestionText, QuestionOptions, QuestionAnswers) VALUES
('Programming', 'What does HTML stand for?', 'Hyper Text Markup Language\nHigh Text Machine Language\nHyper Tabular Markup Language\nNone of the above', 'Hyper Text Markup Language'),
('Programming', 'Which language runs in a web browser?', 'Java\nC\nPython\nJavaScript', 'JavaScript'),
('Programming', 'What symbol is used to denote an array in Python?', 'Parentheses ()\nBrackets []\nBraces {}\nAngle brackets <>', 'Brackets []'),
('Programming', 'What is the correct way to declare a variable in Java?', 'int x\nvar x = 1\nx = int()\nint x = 1', 'int x = 1'),
('Programming', 'Which of the following is a version control software?', 'Slack\nGit\nDocker\nPhotoshop', 'Git'),
('Programming', 'What does CSS stand for?', 'Cascading Style Sheets\nComputer Style Sheets\nCreative Style Sheets\nColorful Style Sheets', 'Cascading Style Sheets'),
('Programming', 'Which of the following is a JavaScript framework?', 'Django\nFlask\nAngular\nLaravel', 'Angular'),
('Programming', 'Which HTML tag is used to define an internal style sheet?', '<css>\n<style>\n<script>\n<link>', '<style>'),
('Programming', 'How do you initialize an array in C++?', 'int arr[5] = {0, 1, 2, 3, 4};\narray<int,5> arr = {0, 1, 2, 3, 4};\nint arr[] = (0, 1, 2, 3, 4);\nAll of the above', 'int arr[5] = {0, 1, 2, 3, 4};'),
('Programming', 'Which of the following is used to define a block of code in Python?', 'Indentation\nBrackets {}\nParentheses ()\nQuotes ""', 'Indentation');

INSERT INTO Questions (CategoryName, QuestionText, QuestionOptions, QuestionAnswers) VALUES
('Database', 'What does SQL stand for?', 'Structured Query Language\nStrong Question Language\nStructured Question List\nNone of the above', 'Structured Query Language'),
('Database', 'Which SQL statement is used to extract data from a database?', 'GET\nSELECT\nEXTRACT\nOPEN', 'SELECT'),
('Database', 'Which SQL statement is used to update data in a database?', 'UPDATE\nMODIFY\nALTER\nCHANGE', 'UPDATE'),
('Database', 'Which SQL statement is used to delete data from a database?', 'REMOVE\nDELETE\nDROP\nCLEAR', 'DELETE'),
('Database', 'How do you select a column named "FirstName" from a table named "People"?', 'SELECT FirstName FROM People\nEXTRACT FirstName FROM People\nCHOOSE FirstName IN People\nGET FirstName FROM People', 'SELECT FirstName FROM People'),
('Database', 'Which keyword is used to sort the result-set in SQL?', 'SORT BY\nORDER BY\nARRANGE BY\nORGANIZE BY', 'ORDER BY'),
('Database', 'What is the default sort order of the "ORDER BY" statement in SQL?', 'Descending\nAscending\nAlphabetical\nNumerical', 'Ascending'),
('Database', 'Which SQL keyword is used to specify a condition that must be met?', 'CONDITION\nWHERE\nMUST\nREQUIRES', 'WHERE'),
('Database', 'Which SQL function is used to count the number of rows in a SQL query?', 'COUNT()\nSUM()\nTOTAL()\nNUMBER()', 'COUNT()'),
('Database', 'What is a primary key?', 'A unique key that can identify each row in a table\nA key that is primary to all databases\nThe first key in a table\nA main key used to sort the table in primary order', 'A unique key that can identify each row in a table');

INSERT INTO Questions (CategoryName, QuestionText, QuestionOptions, QuestionAnswers) VALUES
('Statistics', 'What is the median of the following set of numbers: 2, 7, 4, 9, 3?', '4\n5\n6\n7', '4'),
('Statistics', 'If the mean of a dataset is 20 and its standard deviation is 5, what is the z-score of a value of 25?', '0\n1\n5\n10', '1'),
('Statistics', 'What does a p-value indicate in hypothesis testing?', 'Probability the null hypothesis is true\nProbability the null hypothesis is false\nProbability of making a Type I error\nProbability of making a Type II error', 'Probability of making a Type I error'),
('Statistics', 'Which measure of central tendency is most affected by outliers?', 'Mean\nMedian\nMode\nAll of the above', 'Mean'),
('Statistics', 'What is the range of a dataset that spans from 10 to 50?', '40\n50\n60\n10', '40'),
('Statistics', 'What type of data is measured on a nominal scale?', 'Quantitative data\nOrdinal data\nCategorical data\nContinuous data', 'Categorical data'),
('Statistics', 'Which graph is used to display the distribution of a continuous variable?', 'Bar chart\nHistogram\nPie chart\nLine graph', 'Histogram'),
('Statistics', 'If two events are independent, what is the probability of both events occurring?', 'The sum of the probabilities of each event\nThe product of the probabilities of each event\n0\n1', 'The product of the probabilities of each event'),
('Statistics', 'What is the IQR (Interquartile Range) used to measure?', 'Variability\nCentral tendency\nAssociation between two variables\nNone of the above', 'Variability'),
('Statistics', 'Which test is used to compare the means of more than two groups?', 'T-test\nANOVA\nChi-square test\nPearson correlation', 'ANOVA');

INSERT INTO Questions (CategoryName, QuestionText, QuestionOptions, QuestionAnswers) VALUES
('Business Management', 'Which of the following is a primary function of management?', 'Budgeting\nLeading\nNetworking\nCustomer service', 'Leading'),
('Business Management', 'What does SWOT stand for in strategic planning?', 'Strengths, Weaknesses, Opportunities, Threats\nSavings, Wants, Opportunities, Threats\nStrengths, Wins, Obstacles, Threats\nSolutions, Weaknesses, Opportunities, Techniques', 'Strengths, Weaknesses, Opportunities, Threats'),
('Business Management', 'Which leadership style is characterized by individual control over all decisions and little input from group members?', 'Democratic\nAutocratic\nLaissez-faire\nTransformational', 'Autocratic'),
('Business Management', 'In marketing, what does the 4 Ps stand for?', 'Product, Price, Place, Promotion\nProduct, Planning, Placement, Promotion\nPrice, Placement, Promotion, People\nProduct, Price, People, Process', 'Product, Price, Place, Promotion'),
('Business Management', 'What is the primary goal of financial management?', 'To increase sales\nTo minimize costs\nTo maximize shareholder wealth\nTo promote public interest', 'To maximize shareholder wealth'),
('Business Management', 'Which type of organizational structure is defined by a traditional hierarchy with clear division of labor and centralized decision making?', 'Matrix Structure\nFlat Structure\nHierarchical Structure\nNetwork Structure', 'Hierarchical Structure'),
('Business Management', 'What is the term for the process of gathering, analyzing, and interpreting information about a market, including products and services?', 'Market orientation\nMarket segmentation\nMarket research\nMarket strategy', 'Market research'),
('Business Management', 'Which of the following best describes "corporate social responsibility"?', 'The legal obligation of a corporation to maximize profits for its shareholders\nThe ethical responsibility of a corporation to be accountable to all of its stakeholders\nA marketing strategy to increase a corporation’s product sales\nA financial strategy to increase a corporation’s market share', 'The ethical responsibility of a corporation to be accountable to all of its stakeholders'),
('Business Management', 'What is "benchmarking"?', 'Setting a standard of excellence by comparing to the best in the industry\nA financial strategy to reduce operational costs\nA legal strategy to manage regulatory compliance\nA marketing strategy to identify target customers', 'Setting a standard of excellence by comparing to the best in the industry'),
('Business Management', 'In human resource management, what is "onboarding"?', 'The process of integrating a new employee into the organization\nThe process of evaluating employee performance\nThe process of exiting an employee from the organization\nThe process of recruiting and hiring new employees', 'The process of integrating a new employee into the organization');
