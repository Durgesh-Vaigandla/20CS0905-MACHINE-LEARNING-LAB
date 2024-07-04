# create_database.py
import sqlite3

connection = sqlite3.connect('students.db')
cursor = connection.cursor()

# Create table
cursor.execute('''CREATE TABLE marks
              (roll_no INTEGER PRIMARY KEY,
               mid_term_1_marks_sub1 INTEGER, mid_term_1_marks_sub2 INTEGER, mid_term_1_marks_sub3 INTEGER, mid_term_1_marks_sub4 INTEGER, mid_term_1_marks_sub5 INTEGER,
               mid_term_2_marks_sub1 INTEGER, mid_term_2_marks_sub2 INTEGER, mid_term_2_marks_sub3 INTEGER, mid_term_2_marks_sub4 INTEGER, mid_term_2_marks_sub5 INTEGER)''')

# Insert sample data
cursor.execute('''INSERT INTO marks VALUES
              (1, 32, 35, 38, 30, 31, 35, 36, 39, 33, 34),
              (2, 36, 38, 39, 32, 33, 37, 39, 40, 35, 36),
              (3, 25, 28, 30, 20, 22, 28, 29, 30, 23, 25)''')

connection.commit()
connection.close()
