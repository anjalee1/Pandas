import pandas as pd

df = pd.read_csv('pokemon_data.csv') #to read csv file

#describing data
print(df.describe())#print the statistic details like mean,min,std

#sorting data
print(df.sort_values('Name'))#ascending
print(df.sort_values('Name',ascending= False))#descending
print(df.sort_values(['Type 1','Speed'],ascending= [1,0]))#sorting on the basis of two column values

