import pandas as pd

df = pd.read_csv('pokemon_data.csv') #to read csv file

#aggregrate statistics(group by)

df.groupby(['Type 1']).mean().sort_values('Attack')
df.groupby(['Type 1']).count()
df.groupby(['Type 1']).sum()
df.groupby(['Type 1','Type 2']).mean()#group by two parameters
