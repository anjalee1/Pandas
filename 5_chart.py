
import pandas as pd


df= pd.read_csv("pokemon_data.csv", usecols=['Name','Defense','Attack'])
df =df.head(50)
writer_object = pd.ExcelWriter('pokemon_column_chart.xlsx', engine ='xlsxwriter')
df.to_excel(writer_object, sheet_name ='Poke')


#Create xlsxwriter workbook object
workbook_object = writer_object.book

#Create xlsxwriter worksheet object
worksheet_object = writer_object.sheets['Poke']

# set width of the C and D column
worksheet_object.set_column('C:D', 20)

#create a column chart object that can be added to a worksheet using add_chart() method.
chart_object = workbook_object.add_chart({'type': 'column'})#to create column chart
# chart_object = workbook_object.add_chart({'type': 'line'}) #to create line chart
# chart_object = workbook_object.add_chart({'type': 'scatter'})#to create scatter chart


# Add a data series to a chart
# using add_series method.

# Configure the first series.
# syntax to define ranges is :
# [sheetname, first_row, first_col, last_row, last_col].
chart_object.add_series({
    'name': ['Poke', 0, 2],
    'categories': ['Poke', 1, 1, 50, 1],
    'values': ['Poke', 1, 2, 50, 2],
})

chart_object.add_series({
    'name': ['Poke', 0, 3],
    'categories': ['Poke', 1, 1,50, 1],
    'values': ['Poke', 1, 3,50, 3],
})

# Add a chart title.
chart_object.set_title({'name': 'POKEMON ATTACK AND DEFENSE'})

# Add x-axis label
chart_object.set_x_axis({'name': 'Name'})

# Add y-axis label
chart_object.set_y_axis({'name': 'Attack-Defense'})

# add chart to the worksheet with given
# offset values at the top-left corner of
# a chart is anchored to cell E2
worksheet_object.insert_chart('G2', chart_object,{'x_scale':3,'y_scale':3})
writer_object.save()
