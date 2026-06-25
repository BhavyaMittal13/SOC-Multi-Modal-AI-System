# data_cleaning.py


import pandas as pd
import numpy as np

# CREATING A MESSY DATASET

# Simulating a messy dataset (the kind you'd actually encounter)
np.random.seed(42)

data = {
    "student_id": range(1, 16),
    "age":    [20, 21, 22, np.nan, 20, 21, 22, 23, 20, np.nan, 21, 22, 20, 21, 22],
    "cgpa":   [8.5, 7.2, 9.1, 6.8, np.nan, 8.0, 7.5, 6.5, 9.2, 7.8, 8.1, np.nan, 7.0, 9.5, 6.2],
    "hours_study": [5, 3, 7, 4, 6, np.nan, 5, 8, 7, 4, 5, 6, 3, 8, 999],  # 999 is an outlier!
    "branch": ["CS", "Mech", "CS", "EE", "CS", "Civil", "CS", "EE", None, "CS", "Mech", "CS", "EE", "CS", "CS"],
    "placement": [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1],
}

df = pd.DataFrame(data)

print("="*55)
print("ORIGINAL (MESSY) DATA")
print("="*55)
print(df.to_string())

# STEP 1: INITIAL INSPECTION

print("\n" + "="*55)
print("STEP 1: INSPECTION")
print("="*55)

print("\nShape:", df.shape)
print("\nData types:\n", df.dtypes)

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Percentage of missing values — useful to decide strategy
print("\nMissing value %:")
print((df.isnull().sum() / len(df) * 100).round(1))

# STEP 2: HANDLING MISSING VALUES

print("\n" + "="*55)
print("STEP 2: HANDLING MISSING VALUES")
print("="*55)

# Strategy depends on the column:


df_clean = df.copy()  # always work on a copy!

# Fill missing 'age' with the median (not mean, since age might have outliers)
median_age = df_clean["age"].median()
df_clean["age"].fillna(median_age, inplace=True)
print(f"Filled missing 'age' with median: {median_age}")

# Fill missing 'cgpa' with the mean
mean_cgpa = df_clean["cgpa"].mean()
df_clean["cgpa"].fillna(round(mean_cgpa, 2), inplace=True)
print(f"Filled missing 'cgpa' with mean: {mean_cgpa:.2f}")

# Fill missing 'hours_study' with median (because there's an outlier of 999!)
median_study = df_clean["hours_study"].median()
df_clean["hours_study"].fillna(median_study, inplace=True)
print(f"Filled missing 'hours_study' with median: {median_study}")

# Fill missing 'branch' (categorical) with mode
mode_branch = df_clean["branch"].mode()[0]
df_clean["branch"].fillna(mode_branch, inplace=True)
print(f"Filled missing 'branch' with mode: '{mode_branch}'")

print("\nMissing values after fill:", df_clean.isnull().sum().sum())

# STEP 3: HANDLING OUTLIERS

print("\n" + "="*55)
print("STEP 3: HANDLING OUTLIERS")
print("="*55)


print("\nBefore outlier fix:")
print(f"  hours_study — min: {df_clean['hours_study'].min()}, max: {df_clean['hours_study'].max()}")
print(f"  mean: {df_clean['hours_study'].mean():.2f}, std: {df_clean['hours_study'].std():.2f}")

# Method 1: IQR (Interquartile Range)
Q1 = df_clean["hours_study"].quantile(0.25)
Q3 = df_clean["hours_study"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"\n  Q1={Q1}, Q3={Q3}, IQR={IQR}")
print(f"  Acceptable range: [{lower_bound:.2f}, {upper_bound:.2f}]")

outliers = df_clean[(df_clean["hours_study"] < lower_bound) | (df_clean["hours_study"] > upper_bound)]
print(f"\n  Outlier rows:\n{outliers[['student_id', 'hours_study']]}")

# Replace outliers with the median
median_study_clean = df_clean[
    (df_clean["hours_study"] >= lower_bound) & (df_clean["hours_study"] <= upper_bound)
]["hours_study"].median()

df_clean.loc[df_clean["hours_study"] > upper_bound, "hours_study"] = median_study_clean
df_clean.loc[df_clean["hours_study"] < lower_bound, "hours_study"] = median_study_clean

print(f"\nAfter outlier fix:")
print(f"  hours_study — min: {df_clean['hours_study'].min()}, max: {df_clean['hours_study'].max()}")

# STEP 4: ENCODING CATEGORICAL VARIABLES

print("\n" + "="*55)
print("STEP 4: ENCODING CATEGORICAL VARIABLES")
print("="*55)


print("\nBranch categories:", df_clean["branch"].unique())

# One-Hot Encoding using pd.get_dummies
df_encoded = pd.get_dummies(df_clean, columns=["branch"], prefix="branch", drop_first=False)
print("\nOne-hot encoded columns:", [c for c in df_encoded.columns if "branch_" in c])

# Alternatively, label encoding manually
branch_map = {"CS": 0, "EE": 1, "Mech": 2, "Civil": 3}
df_clean["branch_label"] = df_clean["branch"].map(branch_map)
print("\nLabel-encoded branch:")
print(df_clean[["student_id", "branch", "branch_label"]].head(8))

# STEP 5: FEATURE SCALING

print("\n" + "="*55)
print("STEP 5: FEATURE SCALING")
print("="*55)

# Min-Max Normalization
def min_max_normalize(series):
    return (series - series.min()) / (series.max() - series.min())

# Z-Score Standardization
def z_score_standardize(series):
    return (series - series.mean()) / series.std()

df_clean["cgpa_normalized"]    = min_max_normalize(df_clean["cgpa"]).round(4)
df_clean["cgpa_standardized"]  = z_score_standardize(df_clean["cgpa"]).round(4)

print("\nScaling comparison:")
print(df_clean[["student_id", "cgpa", "cgpa_normalized", "cgpa_standardized"]].head(8))

print(f"\nOriginal CGPA   — min: {df_clean['cgpa'].min():.2f}, max: {df_clean['cgpa'].max():.2f}")
print(f"Normalized       — min: {df_clean['cgpa_normalized'].min():.2f}, max: {df_clean['cgpa_normalized'].max():.2f}")
print(f"Standardized     — mean: {df_clean['cgpa_standardized'].mean():.2f}, std: {df_clean['cgpa_standardized'].std():.2f}")

# FINAL CLEAN DATASET

print("\n" + "="*55)
print("FINAL CLEAN DATASET")
print("="*55)

final_cols = ["student_id", "age", "cgpa", "hours_study", "branch", "placement"]
print(df_clean[final_cols].to_string())
print("\nAll missing values?", df_clean[final_cols].isnull().sum().sum() == 0)
print("Shape:", df_clean[final_cols].shape)
