import json
import pandas as pd

empDetails = {
    "name": ["Ram", "Vinay", "Adhavan"],
    "id": [101, 102, 103],
    "salary": [20000, 20000, 18000],
}

# Write Json file

# with open("emp.json", "w") as emp:
#     json.dump(empDetails, emp, indent=4)


# Read Json file
with open("emp.json", "r") as emp:
    data = json.load(emp)
    print(data)

# Create Data Frame using Json
print("Convert JsonFile to DataFrame....")
df = pd.read_json("emp.json")
print(df)
