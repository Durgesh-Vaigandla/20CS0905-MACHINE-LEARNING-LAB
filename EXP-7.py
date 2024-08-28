import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Read the data
data = pd.read_csv('tennisdata.csv')

# Display the first 5 rows of the data
print("The first 5 values of data are :\n", data.head())

# Split the data into features (X) and target (y)
X = data.iloc[:, :-1]
print("\nThe first 5 values of the training data are:\n", X.head())
y = data.iloc[:, -1]
print("\nThe first 5 values of the target output are:\n", y.head())

# Encode categorical features into numerical values
le_outlook = LabelEncoder()
X['Outlook'] = le_outlook.fit_transform(X['Outlook'])

le_Temperature = LabelEncoder()
X['Temperature'] = le_Temperature.fit_transform(X['Temperature'])

le_Humidity = LabelEncoder()
X['Humidity'] = le_Humidity.fit_transform(X['Humidity'])

le_Windy = LabelEncoder()
X['Windy'] = le_Windy.fit_transform(X['Windy'])

# Display the encoded feature set
print("\nThe encoded training data is:\n", X.head())

# Encode the target variable
le_PlayTennis = LabelEncoder()
y = le_PlayTennis.fit_transform(y)
print("\nThe encoded target output is:\n", y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Train the Naive Bayes classifier
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Evaluate the classifier's accuracy
accuracy = accuracy_score(classifier.predict(X_test), y_test)
print("Accuracy is:", accuracy)