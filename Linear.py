import numpy as np

def linear_regression(X, y, lambda_val=0.01):
    # Add a column of ones to X for the bias term
    X = np.c_[np.ones(X.shape[0]), X]
    
    # Calculate the weights using the normal equation with regularization
    I = np.eye(X.shape[1])
    weights = np.linalg.inv(X.T.dot(X) + lambda_val * I).dot(X.T).dot(y)
    
    return weights

# Example usage
X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([3, 7, 11])

weights = linear_regression(X, y)
print("Weights:", weights)