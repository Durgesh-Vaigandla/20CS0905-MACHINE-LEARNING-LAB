import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Step 1: Data Collection
# Assuming you have a DataFrame 'df' with columns for mid-term marks and 'semester_percentage'
df = pd.read_csv('student_data.csv')

# Step 2: Data Preprocessing
# Selecting all mid-term marks as features
feature_columns = [
    'mid_term_1_marks_sub1', 'mid_term_1_marks_sub2', 'mid_term_1_marks_sub3', 'mid_term_1_marks_sub4', 'mid_term_1_marks_sub5',
    'mid_term_2_marks_sub1', 'mid_term_2_marks_sub2', 'mid_term_2_marks_sub3', 'mid_term_2_marks_sub4', 'mid_term_2_marks_sub5'
]
X = df[feature_columns]  # Features
y = df['semester_percentage']  # Target variable

print(y.shape, X.shape)  
print(X.info())
print(X.columns)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Model Selection and Training
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Model Evaluation
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5

print(f"MAE: {mae}")
print(f"MSE: {mse}")
print(f"RMSE: {rmse}")

# Step 5: Prediction
# Example new data for prediction (assuming marks for all subjects)
new_mid_term_marks = [
    [85, 87, 90, 85, 88, 88, 90, 92, 90, 91],  # Example student 1
    [70, 72, 75, 70, 72, 75, 78, 80, 74, 76],  # Example student 2
    [90, 92, 95, 90, 92, 92, 94, 97, 90, 92]   # Example student 3
]
predicted_percentages = model.predict(new_mid_term_marks)
print(predicted_percentages)
