# model_evaluation.py


import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

np.random.seed(7)

# SETUP: A SIMPLE DATASET

# Simulate: study hours → exam score
n = 60
hours = np.random.uniform(1, 10, n)
# True relationship: score = 8 * hours + 20 + noise
score = 8 * hours + 20 + np.random.normal(0, 5, n)
score = np.clip(score, 0, 100)  # scores can't go below 0 or above 100

X = hours.reshape(-1, 1)
y = score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# PART 1: UNDERSTANDING EACH METRIC

print("="*60)
print("MODEL EVALUATION METRICS — STUDY HOURS vs EXAM SCORE")
print("="*60)

print(f"\nTest set size: {len(y_test)} samples")
print(f"\n{'Sample':>8} {'Actual':>10} {'Predicted':>12} {'Error':>10} {'|Error|':>10}")
print("-" * 55)
errors = []
for i, (actual, pred) in enumerate(zip(y_test[:10], y_pred[:10])):
    err = actual - pred
    errors.append(err)
    print(f"{i+1:>8} {actual:>10.2f} {pred:>12.2f} {err:>+10.2f} {abs(err):>10.2f}")

# ---- MAE: Mean Absolute Error ----
# Average of all |actual - predicted| values
mae = mean_absolute_error(y_test, y_pred)
print(f"\n--- MAE (Mean Absolute Error) ---")
print(f"  MAE = {mae:.2f}")
print(f"  → On average, the model's prediction is off by {mae:.1f} marks")
print(f"  → Treats all errors equally (5-mark error is 5x worse than 1-mark error)")

# ---- MSE: Mean Squared Error ----
# Average of (actual - predicted)²
# Penalizes large errors more heavily than MAE
# Unit: (original unit)² — so for marks, unit is marks²
mse = mean_squared_error(y_test, y_pred)
print(f"\n--- MSE (Mean Squared Error) ---")
print(f"  MSE = {mse:.2f}")
print(f"  → Unit is marks² (harder to interpret directly)")
print(f"  → A 10-mark error contributes 100 to MSE — large errors are punished more")

# ---- RMSE: Root Mean Squared Error ----
# √MSE — brings it back to original units
# More sensitive to outliers than MAE
rmse = np.sqrt(mse)
print(f"\n--- RMSE (Root Mean Squared Error) ---")
print(f"  RMSE = {rmse:.2f}")
print(f"  → Same unit as the target (marks)")
print(f"  → Preferred when large errors are especially bad")

# ---- R² Score ----
# Measures how much variance in y is explained by the model
# Formula: R² = 1 - (SS_res / SS_tot)
#   SS_res = sum of squared errors of our model
#   SS_tot = sum of squared errors of the baseline (just predicting mean)
r2 = r2_score(y_test, y_pred)
print(f"\n--- R² Score (Coefficient of Determination) ---")
print(f"  R² = {r2:.4f}")
print(f"  → The model explains {r2*100:.1f}% of the variance in exam scores")
print(f"  → Perfect model: R² = 1.0")
print(f"  → Baseline (always predict mean): R² = 0.0")
print(f"  → Negative R² means model is WORSE than just predicting the mean")

# Manual R² calculation to understand the formula
ss_res = np.sum((y_test - y_pred) ** 2)      # sum of squared residuals
ss_tot = np.sum((y_test - np.mean(y_test)) ** 2)  # total sum of squares
r2_manual = 1 - (ss_res / ss_tot)
print(f"\n  Manual R² check: {r2_manual:.4f} (should match above)")

# PART 2: COMPARISON — GOOD VS BAD MODEL

print("\n" + "="*60)
print("COMPARING MODELS: Good vs Baseline vs Terrible")
print("="*60)

# Baseline prediction: always predict the mean
y_baseline = np.full_like(y_test, y_train.mean())

# "Terrible" model: random predictions
np.random.seed(99)
y_terrible = np.random.uniform(y_test.min(), y_test.max(), len(y_test))

models = {
    "Our LinearRegression": y_pred,
    "Baseline (mean)":      y_baseline,
    "Random predictions":   y_terrible,
}

print(f"\n{'Model':<25} {'MAE':>8} {'RMSE':>8} {'R²':>8}")
print("-" * 55)
for model_name, preds in models.items():
    m = mean_absolute_error(y_test, preds)
    r = np.sqrt(mean_squared_error(y_test, preds))
    s = r2_score(y_test, preds)
    print(f"{model_name:<25} {m:>8.2f} {r:>8.2f} {s:>8.4f}")

# PART 3: WHEN TO USE WHICH METRIC

print("\n" + "="*60)
print("WHICH METRIC TO USE?")
print("="*60)

print("""
  MAE   → When you want interpretable average error
           → Less sensitive to outliers (a 100-mark error isn't 100x worse than 1-mark)
           → Good for everyday reporting

  MSE   → When large errors are much worse than small ones
           → Used during training (gradient-friendly)
           → Harder to interpret because units are squared

  RMSE  → When you want MSE's sensitivity + interpretable units
           → Most commonly reported metric in regression tasks
           → "On average, my prediction is off by X units"

  R²    → When you want to know relative quality of fit (0-1 scale)
           → Easy to compare across different datasets/scales
           → R² > 0.9 is excellent; R² < 0.5 is poor for simple regression

  Final scores for this task:
""")
print(f"  MAE  = {mae:.2f} marks")
print(f"  RMSE = {rmse:.2f} marks")
print(f"  R²   = {r2:.4f} ({r2*100:.1f}% variance explained)")
print(f"\n  Verdict: {'Good model!' if r2 > 0.8 else 'Needs improvement.'}")
