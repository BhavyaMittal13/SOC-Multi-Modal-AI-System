# train_test_split_demo.py


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

np.random.seed(42)

# PART 1: BASIC TRAIN-TEST SPLIT

print("="*55)
print("BASIC TRAIN-TEST SPLIT")
print("="*55)

# Create dataset
n = 50
X = np.random.rand(n, 2) * 10   # 2 features, values 0-10
y = 3 * X[:, 0] + 2 * X[:, 1] + np.random.normal(0, 2, n)

print(f"\nFull dataset size: {n} samples")

# Split with test_size=0.2 means 20% goes to test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42    # for reproducibility — same split every run
)

print(f"Training set: {X_train.shape[0]} samples ({X_train.shape[0]/n*100:.0f}%)")
print(f"Test set:     {X_test.shape[0]} samples ({X_test.shape[0]/n*100:.0f}%)")

# Train and evaluate
model = LinearRegression()
model.fit(X_train, y_train)

train_score = r2_score(y_train, model.predict(X_train))
test_score  = r2_score(y_test,  model.predict(X_test))

print(f"\nR² on Training data: {train_score:.4f}")
print(f"R² on Test data:     {test_score:.4f}")
print("(Both should be similar — a big gap means overfitting)")



# PART 3: EFFECT OF SPLIT RATIO

print("\n" + "="*55)
print("EFFECT OF SPLIT RATIO")
print("="*55)

# Try different test sizes and see how scores change
print(f"\n{'Test %':>8} {'Train Size':>12} {'Test Size':>10} {'Train R²':>10} {'Test R²':>10}")
print("-" * 55)

for test_frac in [0.1, 0.2, 0.3, 0.4, 0.5]:
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=test_frac, random_state=42)
    m = LinearRegression().fit(Xtr, ytr)
    r2_tr = r2_score(ytr, m.predict(Xtr))
    r2_te = r2_score(yte, m.predict(Xte))
    print(f"{test_frac*100:>7.0f}% {len(Xtr):>12} {len(Xte):>10} {r2_tr:>10.4f} {r2_te:>10.4f}")

print("\nObservation: More training data usually helps, but test set needs to be large enough to be meaningful.")

# PART 4: K-FOLD CROSS VALIDATION

print("\n" + "="*55)
print("K-FOLD CROSS VALIDATION")
print("="*55)


print("\nIdea:")
print("  K=5: split data into 5 parts (folds)")
print("  Fold 1: [TEST] [TRAIN] [TRAIN] [TRAIN] [TRAIN]")
print("  Fold 2: [TRAIN] [TEST] [TRAIN] [TRAIN] [TRAIN]")
print("  Fold 3: [TRAIN] [TRAIN] [TEST] [TRAIN] [TRAIN]")
print("  ... and so on")
print("  Average the 5 test scores → final score")

model_cv = LinearRegression()

# cross_val_score does all the work for us
cv_scores = cross_val_score(model_cv, X, y, cv=5, scoring="r2")

print(f"\n5-Fold CV scores: {cv_scores.round(4)}")
print(f"Mean R²:          {cv_scores.mean():.4f}")
print(f"Std deviation:    {cv_scores.std():.4f}")
print("\nLow std means the model is consistent across different data splits — good sign!")

# Manual K-Fold for understanding
print("\n--- Manual K-Fold walkthrough ---")
kf = KFold(n_splits=5, shuffle=True, random_state=42)
fold_results = []

for fold, (train_idx, test_idx) in enumerate(kf.split(X), 1):
    X_tr, X_te = X[train_idx], X[test_idx]
    y_tr, y_te = y[train_idx], y[test_idx]
    
    m = LinearRegression().fit(X_tr, y_tr)
    score = r2_score(y_te, m.predict(X_te))
    fold_results.append(score)
    
    print(f"  Fold {fold}: Train={len(X_tr)}, Test={len(X_te)}, R²={score:.4f}")

print(f"\n  Average R²: {np.mean(fold_results):.4f}")

# PART 5: RANDOM STATE IMPORTANCE

print("\n" + "="*55)
print("WHY random_state MATTERS")
print("="*55)

print("\nWithout random_state (different split every run):")
for trial in range(3):
    # No random_state = different split each time
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2)
    m = LinearRegression().fit(Xtr, ytr)
    s = r2_score(yte, m.predict(Xte))
    print(f"  Trial {trial+1}: R² = {s:.4f}")

print("\nWith random_state=42 (reproducible):")
for trial in range(3):
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    m = LinearRegression().fit(Xtr, ytr)
    s = r2_score(yte, m.predict(Xte))
    print(f"  Trial {trial+1}: R² = {s:.4f}")

print("\nAlways set random_state for reproducible experiments!")
