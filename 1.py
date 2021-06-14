#loading data into pandas

import pandas as pd

df = pd.read_csv('pokemon_data.csv') #to read csv file
print(df)  # to get data from all the rows
print(df.head(3)) #to get the data from top 3 rows
print(df.tail(3)) #to get the data from bottom 3 rows

#to read from excel file

df_xlsx = pd.read_excel('pokemon_data.xlsx')   #pip install openpyxl
                                               #openpyxl is a python library for reading and writing excel files.
print(df_xlsx)
print(df_xlsx.head(3))
print(df_xlsx.tail(3))


#to read from text file

df = pd.read_csv('pokemon_data.txt',delimiter='\t') # any delimiter separating the columns
print(df.head(4))

#reading data in pandas

#reading headers

print(df.columns)

#reading each column

print(df['HP']) # to read all the rows of column
# or
print(df.HP)# to read all the rows of column
print(df['HP'][0:5]) # to read first five rows of the column
print(df[['Name','HP','Type 1']]) #to read data from 3 columns
#reading each row
print(df.iloc[1])
print(df.iloc[1:4])

for index,row in df.iterrows():
    print(index,row[['Name','HP']])

#reading a specific location

print(df.iloc[2,1])

#getting rows based on specific condition

print(df.loc[df['Type 1'] == "Fire"])


