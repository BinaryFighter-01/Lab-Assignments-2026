# 3_Data Visualization from Extraction Transformation and Loading (ETL) Process

# ETL Process with Visualization

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# EXTRACT
data = {
    "Name": ["Anil","Rahul","Sneha","Priya",
             "Amit","Neha","Rohan","Pooja"],

    "Marks": [85,90,78,88,65,92,70,81]
}

df = pd.DataFrame(data)

# TRANSFORM
df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 80 else "Fail"
)

# LOAD
conn = sqlite3.connect("etl.db")

df.to_sql("students", conn,
          if_exists="replace",
          index=False)

# Read from DB
df = pd.read_sql("SELECT * FROM students", conn)

print(df)

# ---------------- VISUALIZATION ----------------

# 1. Bar Chart
plt.figure()
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 2. Pie Chart
plt.figure()
df["Result"].value_counts().plot.pie(
    autopct="%1.1f%%"
)
plt.title("Pass vs Fail")
plt.ylabel("")
plt.show()

# 3. Line Chart
plt.figure()
plt.plot(df["Name"], df["Marks"], marker="o")
plt.title("Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 4. Histogram
plt.figure()
plt.hist(df["Marks"], bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

conn.close()
