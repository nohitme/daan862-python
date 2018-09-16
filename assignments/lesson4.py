import pandas as pd
import numpy as np

np.random.seed(123)

data = pd.read_csv("/Users/eric.lin/Dropbox/02-School/PSU/daan862/lesson4/Assignment4_data.csv")

print(data[:10])
print(data.describe())

print(data.isnull().sum())
print("total missing values:", data.isnull().values.sum())

# drop missing values
data = data.dropna().reset_index()

# explore "variable" column
print("unique values of 'variable':", data['variable'].unique())

# generate dummies
dummies = pd.get_dummies(data['variable'])
print(dummies[:10])

data_with_dummies = data.join(dummies)
print(data_with_dummies[:10])

# create bins for 'one'
range = data_with_dummies['one'].max() - data_with_dummies['one'].min()
width = range / 3
separator1 = data_with_dummies['one'].min() + width
separator2 = separator1 + width
bins = [-1 * np.inf, separator1, separator2, np.inf]
print("bins:", bins)
res = pd.cut(data_with_dummies['one'], bins)
print("res:\n", pd.value_counts(res))

# Question 2

s = "I am happy to join with you today in what will go down in history as the greatest demonstration for freedom in the history of our nation. Five score years ago, a great American, in whose symbolic shadow we stand today, signed the Emancipation Proclamation. This momentous decree came as a great beacon light of hope to millions of Negro slaves who had been seared in the flames of withering injustice. It came as a joyous daybreak to end the long night of their captivity. But one hundred years later, the Negro still is not free. One hundred years later, the life of the Negro is still sadly crippled by the manacles of segregation and the chains of discrimination. One hundred years later, the Negro lives on a lonely island of poverty in the midst of a vast ocean of material prosperity. One hundred years later, the Negro is still languishing in the corners of American society and finds himself an exile in his own land. So we have come here today to dramatize a shameful condition."

s = s.replace(',', '')
s = s.replace('.', '')
words = s.split(" ")
print(len(words))

lower_case = list(map(lambda x: x.lower(), words))
startWithT = list(filter(lambda x: x.startswith('t'), lower_case))
print(startWithT)
print(len(startWithT))
