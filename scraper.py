import pandas as pd

# Simulated live incoming data (replaceable later with real APIs/sites)
jobs = [
    ["Junior Data Analyst", "PwC", "Johannesburg", 32000, "SQL Excel Python"],
    ["Cloud Support Engineer", "Microsoft", "Johannesburg", 58000, "Azure Linux Python"],
    ["Graduate Data Engineer", "Accenture", "Cape Town", 40000, "SQL Python ETL"],
    ["BI Analyst", "Vodacom", "Pretoria", 45000, "PowerBI SQL Python"],
    ["Junior Software Engineer", "FNB", "Johannesburg", 50000, "Python Git APIs"]
]

df = pd.DataFrame(jobs, columns=["title","company","city","salary","skills"])

# Merge with existing CSV
old = pd.read_csv("jobs.csv")
new_df = pd.concat([old, df], ignore_index=True)

# Remove duplicates
new_df = new_df.drop_duplicates()

# Save updated data
new_df.to_csv("jobs.csv", index=False)

print("Jobs data updated successfully.")
print("Total jobs:", len(new_df))
