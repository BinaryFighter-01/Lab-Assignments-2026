# 2 _Perform the Extraction Transformation and Loading (ETL) process to construct the database in the Sql server / Power BI.

import pandas as pd
import sqlite3

# ------------------ EXTRACT ------------------
# Create sample data (simulate Excel source)
data = {
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Anil", "Rahul", "Sneha", "Priya", "Amit"],
    "Marks": [85, 90, 78, 88, 65]
}

df = pd.DataFrame(data)

# Save and read from Excel (source)
df.to_excel("source.xlsx", index=False)
df = pd.read_excel("source.xlsx")

print("Extracted Data:")
print(df)
print("\n")


# ------------------ TRANSFORM ------------------
# Clean + modify data
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 80 else "Fail")
df["Marks"] = df["Marks"] + 5   # example transformation

print("Transformed Data:")
print(df)
print("\n")


# ------------------ LOAD ------------------
# Load into SQL database
conn = sqlite3.connect("etl.db")
df.to_sql("students", conn, if_exists="replace", index=False)

print("Data loaded into SQL database.\n")

# Verify from DB
result = pd.read_sql("SELECT * FROM students", conn)
print("Data from SQL:")
print(result)

conn.close()