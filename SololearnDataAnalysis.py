"""COVID Data Analysis
You are working with the COVID dataset for California, which includes the number of cases and deaths for each day of 2020.
Find the day when the deaths/cases ratio was largest.
To do this, you need to first calculate the deaths/cases ratio and add it as a column to the DataFrame with the name 'ratio', 
then find the row that corresponds to the largest value.
Important: The output should be a DataFrame, containing all of the columns of the dataset for the corresponding row."""

import pandas as pd

df = pd.read_csv("/usercode/files/ca-covid.csv")

df.drop('state', axis=1, inplace=True)
df.set_index('date', inplace=True)

df['ratio'] = df['deaths'] / df['cases']

maxratio = df['ratio'].max()
print(df[df['ratio']==maxratio])

