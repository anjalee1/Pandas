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


