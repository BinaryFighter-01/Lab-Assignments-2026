# 3_Data Visualization from Extraction Transformation and Loading (ETL) Process

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

#  EXTRACT 
data = {
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Anil", "Rahul", "Sneha", "Priya", "Amit"],
    "Marks": [85, 90, 78, 88, 65]
}

df = pd.DataFrame(data)

#  TRANSFORM
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 80 else "Fail")

# LOAD 
conn = sqlite3.connect("etl.db")
df.to_sql("students", conn, if_exists="replace", index=False)

# Read back from DB (important for ETL proof)
df = pd.read_sql("SELECT * FROM students", conn)

#  VISUALIZATION 

# Bar chart (Name vs Marks)
plt.figure()
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.show()

# Pie chart (Pass vs Fail)
plt.figure()
df["Result"].value_counts().plot.pie(autopct="%1.1f%%")
plt.title("Pass vs Fail")
plt.ylabel("")
plt.show()

conn.close()