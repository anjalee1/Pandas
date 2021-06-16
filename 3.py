import pandas as pd

df = pd.read_csv('pokemon_data.csv') #to read csv file

#filtering the data

df.loc[df['Type 1']== 'Grass']
df.loc[(df['Type 1']== 'Grass') & (df['Speed']== 80) #filtered based on two conditions






