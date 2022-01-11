"""Data frame functions practice"""
import pandas as pd

df = pd.read_csv("housing_dataset.csv")

#print(df.head())

#print (df.tail())

# print(df.info())

# print(df.shape)

# print(df.size)

# print(df.describe())

# print(df.describe(include='all').T)

# print(df.sample(n=5))

# print(df.isnull())

# print(df.isnull().sum())

# print(df.isna())

# print(df.isna().any())

# print(df.nunique())

# print(df.index)

# print(df.columns)

# print(df.memory_usage())

# print(df.nsmallest(5,'median_house_value'))

# print(df.nlargest(5,'median_house_value'))

# print(df.loc[:5,['longitude']])

print(df.iloc[:2,:5])