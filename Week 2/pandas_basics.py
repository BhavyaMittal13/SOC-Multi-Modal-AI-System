# pandas_basics.py

import pandas as pd
import numpy as np

# PART 1: CREATING DATAFRAMES

print("="*50)
print("CREATING DATAFRAMES")
print("="*50)

# From a dictionary (most common way)
data = {
    "name":    ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
    "age":     [22, 25, 21, 23, 24, 22],
    "cgpa":    [8.5, 7.2, 9.1, 6.8, 8.0, 7.5],
    "branch":  ["CS", "Mech", "CS", "EE", "CS", "Civil"],
    "stipend": [15000, 12000, 18000, 11000, 14000, 10000],
}

df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

# From a list of dictionaries (each dict = one row)
records = [
    {"product": "Laptop", "price": 55000, "quantity": 10},
    {"product": "Mouse",  "price": 500,   "quantity": 100},
    {"product": "Desk",   "price": 8000,  "quantity": 20},
]
df_products = pd.DataFrame(records)
print("\nProducts DataFrame:")
print(df_products)

# PART 2: BASIC INSPECTION

print("\n" + "="*50)
print("BASIC INSPECTION")
print("="*50)

# The first thing you should always do with any dataset
print("\nShape (rows, columns):", df.shape)
print("\nColumn names:", list(df.columns))
print("\nData types:\n", df.dtypes)

print("\n df.head() — first 5 rows ")
print(df.head())

print("\n df.tail(3) — last 3 rows ")
print(df.tail(3))

print("\n df.info() — summary ")
df.info()

print("\n df.describe() — statistics for numeric columns ")
print(df.describe())

# PART 3: SELECTING DATA

print("\n" + "="*50)
print("SELECTING DATA")
print("="*50)

# Select one column → returns a Series
print("\nNames column:")
print(df["name"])

# Select multiple columns → returns a DataFrame
print("\nName + CGPA:")
print(df[["name", "cgpa"]])

# Select rows by index (iloc = integer location)
print("\nRow at index 0 (iloc):")
print(df.iloc[0])

print("\nRows 1 to 3 (iloc):")
print(df.iloc[1:4])

# Select rows by label (loc = label-based)
print("\nRow with label 2 (loc):")
print(df.loc[2])

# PART 4: FILTERING

print("\n" + "="*50)
print("FILTERING")
print("="*50)

# Boolean masking — like a where clause in SQL
high_cgpa = df[df["cgpa"] > 8.0]
print("\nStudents with CGPA > 8.0:")
print(high_cgpa)

cs_students = df[df["branch"] == "CS"]
print("\nCS students:")
print(cs_students)

# Multiple conditions — use & (and), | (or), ~ (not)
# IMPORTANT: use parentheses around each condition!
cs_high_cgpa = df[(df["branch"] == "CS") & (df["cgpa"] > 8.0)]
print("\nCS students with CGPA > 8.0:")
print(cs_high_cgpa)

# isin() — filter by multiple values
tech_branches = df[df["branch"].isin(["CS", "EE"])]
print("\nCS or EE students:")
print(tech_branches)

# PART 5: ADDING AND MODIFYING COLUMNS

print("\n" + "="*50)
print("ADDING/MODIFYING COLUMNS")
print("="*50)

# Add a new column
df["annual_stipend"] = df["stipend"] * 12
df["cgpa_category"] = df["cgpa"].apply(
    lambda x: "High" if x >= 8.0 else ("Medium" if x >= 7.0 else "Low")
)

print("\nWith new columns:")
print(df[["name", "cgpa", "cgpa_category", "stipend", "annual_stipend"]])

# PART 6: GROUPBY — AGGREGATION

print("\n" + "="*50)
print("GROUPBY")
print("="*50)

# Group by branch and compute statistics
branch_stats = df.groupby("branch")["cgpa"].agg(["mean", "max", "count"])
branch_stats.columns = ["avg_cgpa", "max_cgpa", "num_students"]
print("\nBranch-wise CGPA statistics:")
print(branch_stats)

# Groupby with multiple aggregations on multiple columns
summary = df.groupby("branch").agg(
    avg_cgpa   = ("cgpa", "mean"),
    avg_stipend= ("stipend", "mean"),
    count      = ("name", "count")
)
print("\nFull branch summary:")
print(summary)

# PART 7: SORTING

print("\n" + "="*50)
print("SORTING")
print("="*50)

sorted_df = df.sort_values("cgpa", ascending=False)
print("\nSorted by CGPA (descending):")
print(sorted_df[["name", "branch", "cgpa"]])

# Sort by multiple columns
sorted_multi = df.sort_values(["branch", "cgpa"], ascending=[True, False])
print("\nSorted by branch (A-Z) then CGPA (high to low):")
print(sorted_multi[["name", "branch", "cgpa"]])

# PART 8: USEFUL UTILITIES

print("\n" + "="*50)
print("USEFUL UTILITIES")
print("="*50)

# Value counts
print("\nBranch distribution:")
print(df["branch"].value_counts())

# Unique values
print("\nUnique branches:", df["branch"].unique())

# Correlation matrix (numeric columns only)
print("\nCorrelation matrix:")
print(df[["age", "cgpa", "stipend"]].corr())

# Apply a function to a column
df["cgpa_scaled"] = df["cgpa"].apply(lambda x: (x - df["cgpa"].mean()) / df["cgpa"].std())
print("\nNormalized CGPA (z-scores):")
print(df[["name", "cgpa", "cgpa_scaled"]].round(3))
