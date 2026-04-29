import pandas as pd

# Load the CSV file
df = pd.read_csv("jobs.csv")

# Show all data
print("=== FULL DATASET ===")
print(df)

# Basic stats
print("\n=== TOTAL JOBS ===")
print(len(df))

print("\n=== AVERAGE SALARY ===")
print("R", round(df["salary"].mean(), 2))

print("\n=== JOBS BY CITY ===")
print(df["city"].value_counts())

print("\n=== TOP PAYING JOB ===")
print(df.loc[df["salary"].idxmax()])
