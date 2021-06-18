import pandas as pd

df = pd.read_csv('pokemon_data.csv',) #to read csv file

#boolean indexing

 #Accessing a DataFrame with a boolean index
data = df.head(5)
data.index=[True, False, True, False,True]
data =data.drop(columns=['#'])
print(data)
print(data.loc[True])
#In order to access a dataframe using .iloc[], we have to pass a boolean
# value (True or False)  but iloc[] function accept only integer as argument so
# it will throw an error if we pass  boolean  value (True or False) ]
print(data.iloc[0:5])

#Applying a boolean mask to a dataframe
data = df.head(5)
data = data.drop(columns=['#'])
print(data[[True, False, True, False,True]])# When we apply a boolean mask it will
                                            #print only that dataframe in which we pass a boolean value True.
