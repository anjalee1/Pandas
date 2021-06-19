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
