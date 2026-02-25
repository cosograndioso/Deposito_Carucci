import pandas as pd

file_path = 'vendite.csv'

df = pd.read_csv(file_path)

print(df.head())