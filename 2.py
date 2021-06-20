import pandas as pd

df = pd.read_csv('pokemon_data.csv') #to read csv file

#describing data
print(df.describe())#print the statistic details like mean,min,std

#sorting data
print(df.sort_values('Name'))#ascending
print(df.sort_values('Name',ascending= False))#descending
print(df.sort_values(['Type 1','Speed'],ascending= [1,0]))#sorting on the basis of two column values

#making changes to the data
df['Total'] = df['HP'] + df['Speed']+df['Attack']  #to add new column
df= df.drop(columns=['Total']) #to drop a column
df['Total'] = df.iloc[:,4:10].sum(axis=1)#add new column where axis = 1 means add horizontally and 0 means add vertically

#to rearrange the columns
cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]]+cols[4:12]] 

#exporting the data to desired format
df.to_csv('modified.csv', index=False)
df.to_excel('modified.xlsx', index=False)
df.to_csv('modified.txt', index=False, sep='\t')
