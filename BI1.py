# 1 _Import Data from different Sources such as (Excel, Sql Server, Oracle etc.) and load in targeted system.
import pandas as pd
import sqlite3

# Create sample dataset (simulating source data)
data = {
    "ID": [1, 2, 3, 4],
    "Name": ["Anil", "Rahul", "Sneha", "Priya"],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

# Save data to Excel (data source)
df.to_excel("input_data.xlsx", index=False)

# Load data from Excel
excel_df = pd.read_excel("input_data.xlsx")

# Connect to SQL database
conn = sqlite3.connect("student.db")

# Store data into database table
excel_df.to_sql("students", conn, if_exists="replace", index=False)

# Fetch data from database
sql_df = pd.read_sql("SELECT * FROM students", conn)

# Simple transformation (add result column)
sql_df["Result"] = sql_df["Marks"].apply(lambda x: "Pass" if x >= 80 else "Fail")

# Load final data into target system (CSV)
sql_df.to_csv("output_data.csv", index=False)

# Close database connection
conn.close()

