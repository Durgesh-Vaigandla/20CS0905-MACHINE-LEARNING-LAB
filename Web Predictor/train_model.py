# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Sample data
data = {
    'mid_term_1_marks_sub1': [32, 36, 25, 39, 30, 35, 20, 33, 28, 34],
    'mid_term_1_marks_sub2': [35, 38, 28, 40, 32, 36, 22, 35, 30, 36],
    'mid_term_1_marks_sub3': [38, 39, 30, 40, 34, 38, 24, 37, 32, 38],
    'mid_term_1_marks_sub4': [30, 32, 20, 36, 28, 33, 18, 30, 25, 32],
    'mid_term_1_marks_sub5': [31, 33, 22, 38, 30, 34, 19, 31, 26, 33],
    'mid_term_2_marks_sub1': [35, 37, 28, 40, 32, 37, 22, 34, 30, 36],
    'mid_term_2_marks_sub2': [36, 39, 29, 40, 33, 38, 23, 36, 31, 38],
    'mid_term_2_marks_sub3': [39, 40, 30, 40, 35, 39, 25, 38, 33, 39],
    'mid_term_2_marks_sub4': [33, 35, 23, 38, 30, 36, 20, 32, 27, 35],
    'mid_term_2_marks_sub5': [34, 36, 25, 39, 31, 37, 21, 33, 28, 36],
    'semester_percentage': [84, 90, 76, 94, 80, 91, 66, 87, 77, 91]
}

df = pd.DataFrame(data)

# Features and target
features = [
    'mid_term_1_marks_sub1', 'mid_term_1_marks_sub2', 'mid_term_1_marks_sub3', 'mid_term_1_marks_sub4', 'mid_term_1_marks_sub5',
    'mid_term_2_marks_sub1', 'mid_term_2_marks_sub2', 'mid_term_2_marks_sub3', 'mid_term_2_marks_sub4', 'mid_term_2_marks_sub5'
]
X = df[features]
y = df['semester_percentage']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'marks_predictor_model.pkl')
