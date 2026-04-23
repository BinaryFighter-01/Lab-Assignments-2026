"""Real estate agents want help to predict the house price for regions in the USA.
He gave you the dataset to work on and you decided to use the Linear Regression Model. Create a
model that will help him to estimate what the house would sell for.
URL for a dataset:
https://github.com/huzaifsayed/Linear-Regression-Model-for-House-PricePrediction/blob/master/USA_Housing.csv"""


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np

# Load dataset
url = "https://raw.githubusercontent.com/bcbarsness/machine-learning/master/USA_Housing.csv"
data = pd.read_csv(url)

# Features and target
X = data[['Avg. Area Income', 'Avg. Area House Age',
          'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms',
          'Area Population']]
y = data['Price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluation metrics
mae = metrics.mean_absolute_error(y_test, predictions)
rmse = np.sqrt(metrics.mean_squared_error(y_test, predictions))

print("MAE:", mae)
print("RMSE:", rmse)


# What they actually mean
# MAE = 81,618.02 → On average, your prediction is off by ~$81k
# RMSE = 100,796.65 → Typical error is ~$100k, but penalizes big mistakes more

#  These are in same unit as target (Price) → dollars 