"""Real estate agents want help to predict the house price for regions in the USA.
He gave you the dataset to work on and you decided to use the Linear Regression Model. Create a
model that will help him to estimate what the house would sell for.
URL for a dataset:
https://raw.githubusercontent.com/huzaifsayed/Linear-Regression-Model-for-House-Price-Prediction/refs/heads/master/USA_Housing.csv"""


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Load Dataset
url = "https://raw.githubusercontent.com/bcbarsness/machine-learning/master/USA_Housing.csv"

df = pd.read_csv(url)

# Features and Target
X = df[['Avg. Area Income',
        'Avg. Area House Age',
        'Avg. Area Number of Rooms',
        'Avg. Area Number of Bedrooms',
        'Area Population']]

y = df['Price']

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

# Create and Train Model
model = LinearRegression()

model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

# Evaluation
mae = metrics.mean_absolute_error(y_test, pred)

rmse = np.sqrt(metrics.mean_squared_error(y_test, pred))

# Output
print("----- House Price Prediction -----\n")

print("Sample Predictions:\n")

for i in range(5):

    print("Actual Price    :", round(y_test.iloc[i], 2))

    print("Predicted Price :", round(pred[i], 2))

    print()

print("MAE  =", round(mae, 2))

print("RMSE =", round(rmse, 2))


# What they actually mean
# MAE = 81,618.02 → On average, your prediction is off by ~$81k
# RMSE = 100,796.65 → Typical error is ~$100k, but penalizes big mistakes more

#  These are in same unit as target (Price) → dollars 
