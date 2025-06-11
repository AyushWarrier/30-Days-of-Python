# Day 22: Pandas for Data Analysis

import pandas as pd 

# Creating a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 30, 22, 35],
    "City": ["New York", "London", "Paris", "Tokyo"]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

print("\nFirst 2 rows:\n", df.head(2))
print("\nSummary Info:")
df.info()
print("\nStatistical Summary:\n", df.describe(include="all"))

print("\nName column:\n", df["Name"])
print("\nRow 0:\n", df.loc[0])
print("\nSecond row (by position):\n", df.iloc[1])

print("\nPeople older than 25:\n", df[df["Age"] > 25])

df["Is_Adult"] = df["Age"] >= 18
print("\nWith 'Is_Adult' column:\n", df)

df.at[0, "City"] = "San Francisco"
print("\nAfter modifying Alice's city:\n", df)

# Exporting to CSV (this will create a file if run locally)
# df.to_csv("people.csv", index=False)
