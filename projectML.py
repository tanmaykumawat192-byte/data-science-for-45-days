import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load Dataset
url = "https://raw.githubusercontent.com/tanmaykumawat192-byte/data-science-for-45-days/refs/heads/main/Housing_Selected.csv"
df = pd.read_csv(url)

# Display Dataset
print(df.head())
print(df.info())
print(df.isnull().sum())

# Features and Target
X = df[['area', 'bedrooms', 'bathrooms', 'stories', 'parking']]
y = df['price']

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction on Test Data
y_pred = model.predict(X_test)

# Predict New House Price
new_data = pd.DataFrame({
    'area': [6000],
    'bedrooms': [3],
    'bathrooms': [2],
    'stories': [2],
    'parking': [1]
})

predicted_price = model.predict(new_data)

print(f"\nPredicted Price: ₹{predicted_price[0]:,.2f}")

# Model Evaluation
print("\nR2 Score:", r2_score(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# Actual vs Predicted Graph
plt.figure(figsize=(10,6))

plt.scatter(range(len(y_test)), y_test,
            color='blue', label='Actual Price')

plt.scatter(range(len(y_pred)), y_pred,
            color='red', label='Predicted Price')

plt.xlabel("House Number")
plt.ylabel("Price")
plt.title("Actual vs Predicted House Prices")
plt.legend()

plt.show()