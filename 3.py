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
       

#filtering data based on textual pattern(regex filtering)
       
df.loc[df['Name'].str.contains('Mega')]#filter rows that contains Mega
df.loc[~df['Name'].str.contains('Mega')] #filter rows that does not contains Mega

import re
       
df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)] #this flag will ignore case
df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
       
#conditional changes
   
df.loc[df['Type 1']== 'Fire','Type 1'] = 'Flamer'
df.loc[df['Type 1']== 'Fire','Legendary'] = True #parameter does not to be the same column
df.loc[df['HP']<50,['Generation','Legendary']]= 'same value' #changing two columns at the same time with same value 
df.loc[df['HP']<50,['Generation','Legendary']]= ['diff1','diff2] #changing two columns at the same time with different value 
 
 




