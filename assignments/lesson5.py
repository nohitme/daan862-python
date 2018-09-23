import pandas as pd
import numpy as np

np.random.seed(123)

data1 = pd.read_csv("/Users/eric.lin/Dropbox/02-School/PSU/daan862/lesson5/data1.csv")
data2 = pd.read_csv("/Users/eric.lin/Dropbox/02-School/PSU/daan862/lesson5/data2.csv")

print("data 2")
print(data2[:10])

# data 3 = set ID and variable of data 2
data3 = data2.set_index(['ID', 'variable'])
print(data3[:10])

# get aggregated mean of 'variable'
print(data3.mean(level='variable'))

# preview data 1
print("data 1")
print(data1[:10])

# data 4 = melt the ID from data 1
data4 = data1.melt('ID')
data4_indexed = data4.set_index(['ID', 'variable'])
print(data4_indexed.mean(level='variable'))

# data 5 = data2 -> data1
data5 = data2.pivot('ID', 'variable', 'value').reset_index()
print(data5)

# data 6 = data 1 + data 5
# note: we have multiple ways to "merge" data 1 and data 5
# when using default "inner" join, the result will be an empty dataframe
# since data 1 has more ID values. Therefore I use "outer" join here.
# also we could join on 'ID' column and the result will have 9 columns (including ID)
data6 = pd.merge(data1, data5, how='outer')
print(data6.describe())
print(data6.sum())

# group by 'ID'
data6_grouped = data6.set_index('ID')
print(data6_grouped.sum(level='ID'))
print(data6_grouped.mean(level='ID'))
