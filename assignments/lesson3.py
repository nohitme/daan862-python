from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
# increase the max column display to avoid truncation in console outputs
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option("display.max_columns", 11)
# np.set_printoptions(linewidth=desired_width)

path = "/Users/eric.lin/Dropbox/02-School/PSU/daan862"
os.chdir(path)

mtcars = pd.read_csv("mtcars.csv")

print(mtcars.describe())
print(mtcars.corr())
print(mtcars.cov())

# add new column company
mtcars['company'] = mtcars.model.str.split(' ', expand=True)[0]

merc = mtcars.loc[mtcars['company'] == 'Merc']
merc = merc.reset_index(drop=True)
print(merc)
print(merc.describe())
print(mtcars.corr())
print(mtcars.cov())

non_merc = mtcars.loc[mtcars['company'] != 'Merc']
print("mean mpg of Merc:", round(merc.mpg.mean(), 3), "and mean mpg of others:", round(non_merc.mpg.mean(), 3))

