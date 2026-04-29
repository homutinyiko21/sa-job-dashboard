import pandas as pd

# Load data
df = pd.read_csv("jobs.csv")

# Average salary by title
avg_salary = df.groupby("title")["salary"].mean()

print("=== Predicted Salary by Historical Average ===")

job = "Data Engineer"

if job in avg_salary.index:
    print(f"{job}: R{avg_salary[job]:,.0f}")
else:
    print("Job not found in dataset")

