"""5 _Perform the data classification algorithm using any Classification algorithm."""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Dataset 
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 40, 50, 55, 65, 70, 80, 90],
    "Result": [0, 0, 0, 1, 1, 1, 1, 1]   # 0=Fail, 1=Pass
}

df = pd.DataFrame(data)

# Split 
X = df[["Hours", "Marks"]]
y = df["Result"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model 
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction 
y_pred = model.predict(X_test)

# Evaluation 
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)

# Test sample
print("Prediction (5 hrs, 60 marks):", model.predict([[5, 60]]))