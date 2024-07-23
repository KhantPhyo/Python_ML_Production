import pandas as pd

# define a dictionary containing student data
data = {'Name': ['John', 'Emma', 'Michael', 'Sophia'],
       'Height': [5.5, 6.0, 5.8, 5.3],
       'Qualification': ['BSc', 'BBA', 'MBA', 'BSc']}

# convert the dictionary into a DataFrame
df = pd.DataFrame(data)
print("Original DF : ",df)

# declare a new list
address = ['New York', 'London', 'Sydney', 'Toronto']

# assign the list as a column
df['Address'] = address

print("Modified DF : ",df)