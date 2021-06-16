import pandas as pd

df = pd.read_csv('pokemon_data.csv') #to read csv file

#filtering the data

df.loc[df['Type 1']== 'Grass']
df.loc[(df['Type 1']== 'Grass') & (df['Speed']== 80) #filtered based on two conditions
df.loc[(df['Type 1']== 'Grass') | (df['Speed']== 80)]
       
#resetting index
# df_new = df.loc[(df['Type 1']== 'Grass') & (df['Speed']== 80) & (df['HP'] >70)].reset_index() #storing data to new data frame and resetting the index so that it will start from 0
df_new = df.loc[(df['Type 1']== 'Grass') & (df['Speed']== 80) & (df['HP'] >70)].reset_index(drop=True)#use drop parameter to remove index from older dataframe
print(df_new)
       






