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
#some of the important parameters used with read_csv

# makes the passed rows header
df =pd.read_csv("pokemon_data.csv", header=[1, 2])

# make the passed column as index instead of 0, 1, 2, 3....
 df =pd.read_csv("pokemon_data.csv", index_col='Type 1')

# uses passed cols only for data frame
df= pd.read_csv("pokemon_data.csv", usecols=["Type 1",'Type 2'])

# returuns pandas series if there is only one colunmn
df=pd.read_csv("pokemon_data.csv", usecols=["Type 1",'Type 2'],squeeze=True)

# skips the passed rows in new series
df =pd.read_csv("pokemon_data.csv",skiprows=[1, 2, 3, 4])

#writing Excel files using the XlsxWriter modules

df = pd.DataFrame({'Data': ['nikola', 'einstein', 'carl', 'marie',
                            'neil', 'hawking', 'michio']})
df1 = pd.DataFrame({'Data': ['data1', 'data2', 'data3', 'data4',
                            'data5', 'data6', 'data7']})

df2=pd.DataFrame({'Data': ['data8', 'data9', 'data10', 'data11',
                            'data12', 'data13', 'data14']})
df3=pd.DataFrame({'Data': ['data15', 'data16', 'data17', 'data18',
                            'data19', 'data20', 'data21']})

 #Writing multiple dataframes to worksheets using Pandas and XlsxWriter.
writer = pd.ExcelWriter('sci1.xlsx',engine='xlsxwriter')
df.to_excel(writer, sheet_name ='Sheet1')
df1.to_excel(writer, sheet_name ='Sheet2')
df2.to_excel(writer, sheet_name ='Sheet3')
df3.to_excel(writer, sheet_name ='Sheet4')

 # writing and Positioning the dataframes in the worksheet.
df.to_excel(writer, sheet_name='Sheet5')
df1.to_excel(writer, sheet_name='Sheet5', startcol=3)
df2.to_excel(writer, sheet_name='Sheet5', startrow=9)
df3.to_excel(writer, sheet_name ='Sheet5',startcol=3,startrow=9)
writer.save()
