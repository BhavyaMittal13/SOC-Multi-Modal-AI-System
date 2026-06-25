# linear_regression.py


import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib
matplotlib.use('Agg')  # no display needed — saves to file if needed
import matplotlib.pyplot as plt

# PART 1: SIMPLE LINEAR REGRESSION
# (one feature → one output)

print("="*55)
print("SIMPLE LINEAR REGRESSION")
print("(House area vs Price)")
print("="*55)

# Generate synthetic data: house size → price
np.random.seed(0)
house_size = np.array([600, 800, 1000, 1200, 1400, 1600, 1800, 2000,
                        2200, 2400, 2600, 2800, 3000, 3200, 3400])  # sq ft
# Price = 50*size + some random noise (so we know the true relationship)
price = 50 * house_size + np.random.normal(0, 15000, len(house_size))  # in rupees (thousands)

print(f"\nData (first 5 rows):")
for i in range(5):
    print(f"  Size: {house_size[i]} sqft → Price: ₹{price[i]:.0f}k")

# Reshape for sklearn — needs 2D array for X
X = house_size.reshape(-1, 1)   # shape becomes (15, 1) instead of (15,)
y = price

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Inspect what the model learned
print(f"\nModel learned:")
print(f"  Coefficient (slope): {model.coef_[0]:.2f}")
print(f"  Intercept:           {model.intercept_:.2f}")
print(f"\nInterpretation: For every 1 sqft increase in size,")
print(f"  the price increases by ₹{model.coef_[0]:.2f}k")

# Predictions
y_pred = model.predict(X_test)

print(f"\nPredictions vs Actual:")
print(f"{'Actual':>12} {'Predicted':>12} {'Error':>10}")
for actual, pred in zip(y_test, y_pred):
    error = actual - pred
    print(f"₹{actual:>10.0f}k  ₹{pred:>10.0f}k  {error:>+9.0f}k")

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"\n--- Model Performance ---")
print(f"  MAE  (Mean Absolute Error):  {mae:.2f}k")
print(f"  RMSE (Root Mean Sq Error):   {rmse:.2f}k")
print(f"  R²   (R-squared Score):      {r2:.4f}")

# PART 2: MULTIPLE LINEAR REGRESSION
# (multiple features → one output)

print("\n" + "="*55)
print("MULTIPLE LINEAR REGRESSION")
print("(Area + Rooms + Age → Price)")
print("="*55)

# Generate synthetic multi-feature dataset
np.random.seed(1)
n = 100

area     = np.random.randint(500, 3500, n)
rooms    = np.random.randint(1, 6, n)
age      = np.random.randint(0, 30, n)

# True price formula (known to us, model has to figure it out)
price_multi = (
    60 * area
    + 5000 * rooms
    - 2000 * age
    + np.random.normal(0, 20000, n)  # noise
)

# Build DataFrame
df = pd.DataFrame({
    "area":  area,
    "rooms": rooms,
    "age":   age,
    "price": price_multi
})

print(f"\nDataset shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nStats:\n{df.describe().round(1)}")

# Features and target
X_multi = df[["area", "rooms", "age"]]
y_multi = df["price"]

X_tr, X_te, y_tr, y_te = train_test_split(X_multi, y_multi, test_size=0.2, random_state=42)

# Train
model_multi = LinearRegression()
model_multi.fit(X_tr, y_tr)

# Coefficients
print(f"\nModel coefficients:")
for feature, coef in zip(X_multi.columns, model_multi.coef_):
    print(f"  {feature:<8}: {coef:>10.2f}")
print(f"  intercept: {model_multi.intercept_:>10.2f}")

# Compare to true values (approximately):
# area: 60, rooms: 5000, age: -2000

# Evaluate
y_pred_multi = model_multi.predict(X_te)
r2_multi = r2_score(y_te, y_pred_multi)
rmse_multi = np.sqrt(mean_squared_error(y_te, y_pred_multi))

print(f"\nMultiple Regression Performance:")
print(f"  R² Score:  {r2_multi:.4f}")
print(f"  RMSE:      ₹{rmse_multi:.0f}")

# PART 3: PREDICT ON NEW DATA

print("\n" + "="*55)
print("MAKING NEW PREDICTIONS")
print("="*55)

# Predict price of a new house: 1800 sqft, 3 rooms, 5 years old
new_house = pd.DataFrame({
    "area": [1800],
    "rooms": [3],
    "age": [5]
})

predicted_price = model_multi.predict(new_house)[0]
print(f"\nNew house: 1800 sqft, 3 rooms, 5 years old")
print(f"Predicted price: ₹{predicted_price:.0f}")

# Sanity check: true formula gives 60*1800 + 5000*3 - 2000*5 = 108000 + 15000 - 10000 = 113000
manual = 60 * 1800 + 5000 * 3 - 2000 * 5
print(f"Manual calculation (no noise): ₹{manual}")
print(f"Close? {'Yes' if abs(predicted_price - manual) < 20000 else 'Not exactly (noise effect)'}")
