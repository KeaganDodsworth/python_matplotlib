import pandas as pd
from pandas import ExcelFile

df = pd.read_excel('data.xlsx', sheet_name = 'Sheet1')
 
X = list(df['X'])
Y = list(df['Y'])

print(X)
print(Y)
