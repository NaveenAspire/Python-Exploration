import pandas as pd

print("Series Result.......")
# Pandas Series

name = ["Ram", "Vinay", "Adhavan"]
# series = pd.Series(name)
series = pd.Series(name, index=[1, 2, 3])
print(series)
print()
print(series[1])
print()

print("DataFrame Result........")
# Pandas Data Frame

empDetails = {
    "name": ["Ram", "Vinay", "Adhavan"],
    "id": [101, 102, 103],
    "salary": [20000, 20000, 18000],
}
df = pd.DataFrame(empDetails, index=["Team A", "Team B", "Team C"])
print(df)
print()
print(df.loc["Team A"])
print()
print(df.loc[["Team A", "Team C"]])

print(df.head())

print(df.tail())

print(df.min(numeric_only=True))
