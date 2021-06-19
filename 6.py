import pandas as pd

df= pd.read_csv("pokemon_data.csv", usecols=['Name','Speed','Attack'],nrows=6)

#add new column to existing dataframe

new_col=['col1','col2','col3','col4','col5','col6']
df['AU-col'] = new_col #method1
df.insert(2, "Anjali", [1, 2, 3, 4,5,6], True) #method2- using insert()
df=df.assign(Nickname = ['Bul', 'Ivy', 'Ven', 'venus','charm','charl'])#method3- using assign()
print(df)

#truncate dataframe

result = df.truncate(before=2, after=4)
print(result)

#Iterating over rows

for i, j in df.iterrows(): #method1- using iterrows()
    print(i, j)
    print()

for key, value in df.iteritems(): #method2- using iteritems()
    print(key, value)
    print()

for i in df.itertuples():#method3- using itertuples()
    print(i)

#Iterating over Columns

# creating a list of dataframe columns
columns = list(df)

for i in columns:
    # printing the third element of the column
    print(df[i][2])

#Working with Missing Data
#Checking for missing values using isnull() and notnull()

df= pd.read_csv("pokemon_data.csv", usecols=['Name','Type 1','Type 2'],nrows=6)
print(df.isnull())#return dataframe of Boolean values which are True for NaN values.
print(df.notnull())#return dataframe of Boolean values which are False for NaN values.
