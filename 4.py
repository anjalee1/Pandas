import pandas as pd

df = pd.read_csv('pokemon_data.csv') #to read csv file

#aggregrate statistics(group by)

df.groupby(['Type 1']).mean().sort_values('Attack')
df.groupby(['Type 1']).count()
df.groupby(['Type 1']).sum()
df.groupby(['Type 1','Type 2']).mean()#group by two parameters

#working with large amounts of data
for df in pd.read_csv('pokemon_data.csv' , chunksize= 5):# reading data in chunks
    print(df)
    
    
new_df= pd.DataFrame(columns =df.columns)

for df in pd.read_csv('pokemon_data.csv' , chunksize= 5):# reading data in chunks
    results = df.groupby(['Type 1']).count()
    new_df =pd.concat([new_df,results])
    new_df = new_df.loc[: ,new_df.columns !='Type 1'] # stores all columns except 'Type 1'
    print(new_df)
    
#creating pandas dataframe

df = pd.DataFrame(data=[[1,2,3],[4,5,6],[7,8,9]],index = ['row1','row2','row3'],columns=['col1','col2','col3'])
print(df)

lst=['tesla', 'carl sagan', 'einstein']
df1 =pd.DataFrame(lst)#Creating dataframe using list
print(df1)

dct ={'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]}
df2 = pd.DataFrame(dct)#Creating dataframe using dictionary
print(df2)

#pandas series

df = pd.read_csv('pokemon_data.csv')

ser= pd.Series(df['Name']) #creating a series
# print(ser)

#binary operation on series

ser1 =pd.Series(df['Attack'])
ser2 =pd.Series(df['Sp. Atk'])

print(ser1.add(ser2).head(5))
print(ser1.sub(ser2).head(5))

#conversion operation on series
#conversion of type
before = df.dtypes
print(before)

df['Defense'] =df['Defense'].astype(str)
df['Sp. Def'] =df['Sp. Def'].astype(str)

after = df.dtypes
print(after)

  #conversion to list

dtype_before = type(df['HP'])
print(dtype_before)

hp_list= df['HP'].tolist()
dtype_after = type(hp_list)
print(dtype_after)
