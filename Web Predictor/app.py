# app.py
from flask import Flask, request, jsonify, render_template
import sqlite3
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('marks_predictor_model.pkl')

# Define the features
features = [
    'mid_term_1_marks_sub1', 'mid_term_1_marks_sub2', 'mid_term_1_marks_sub3', 'mid_term_1_marks_sub4', 'mid_term_1_marks_sub5',
    'mid_term_2_marks_sub1', 'mid_term_2_marks_sub2', 'mid_term_2_marks_sub3', 'mid_term_2_marks_sub4', 'mid_term_2_marks_sub5'
]

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    roll_no = int(request.form['roll_no'])
    
    # Fetch mid-term marks from the database
    connection = sqlite3.connect('students.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM marks WHERE roll_no=?", (roll_no,))
    record = cursor.fetchone()
    connection.close()
    
    if record:
        student_data = list(record[1:])  # Skip the roll_no column
        df = pd.DataFrame([student_data], columns=features)
        prediction = model.predict(df)[0]
        return jsonify({'roll_no': roll_no, 'predicted_percentage': prediction})
    else:
        return jsonify({'error': 'Roll number not found in the database'})

if __name__ == '__main__':
    app.run(debug=True)
