import csv
import pandas as pd

empDetails = [
    {"name": "Ram", "id": 101, "salary": 20000},
    {"name": "Vinay", "id": 102, "salary": 20000},
    {"name": "Adhavan", "id": 103, "salary": 18000},
]

fields = ["name", "id", "salary"]

with open("emp.csv", "w") as emp:
    csvwriter = csv.DictWriter(emp, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerows(empDetails)

# Create Data Frame using CSV file
df = pd.read_csv("emp.csv")
print(df)
