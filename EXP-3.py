"""
Implement Naïve Bayes theorem to classify the English text
"""
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
newsgroups = fetch_20newsgroups(subset='all')

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(newsgroups.data, newsgroups.target, test_size=0.2, random_state=42)

# Create a pipeline to streamline the process
text_clf = Pipeline([
    ('vect', CountVectorizer()),       # Convert text to word counts
    ('tfidf', TfidfTransformer()),     # Transform word counts to TF-IDF features
    ('clf', MultinomialNB())           # Train a Naive Bayes classifier
])

# Train the model
text_clf.fit(X_train, y_train)

# Make predictions
y_pred = text_clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.4f}')
print('Classification Report:')
print(classification_report(y_test, y_pred, target_names=newsgroups.target_names))
