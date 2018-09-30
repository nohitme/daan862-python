#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 18:31:56 2018

@author: eric.lin
"""

import matplotlib.pyplot as plt
import pandas as pd
import os

# Change the working directory
os.chdir("/Users/eric.lin/Dropbox/02-School/PSU/daan862/lesson6")
mtcars = pd.read_csv('mtcars.csv')

# histgram of mpg by am
mtcars.groupby("am").mpg.hist(alpha = 0.4, grid = True)
plt.savefig("hist.png")

# scatter plot of mpg VS. hp
cmap = mtcars.cyl.factorize()[0]
mtcars.plot.scatter(x = 'hp', y = 'mpg', s = 50, c = cmap, grid = True)
plt.savefig("scatter.png")

# a scatterplot matrix for new data consisting of columns [disp, hp, drat, wt, qsect]
plt.style.use('classic')
mtcars_matrix = mtcars[['disp', 'hp', 'drat', 'wt', 'qsec']]
pd.plotting.scatter_matrix(mtcars_matrix, s = 50, diagonal = 'kde', c = cmap)
plt.savefig("scatter-matrix.png")

# Create boxplots for new data consisting of columns [disp, hp, drat, wt, qsect].
mtcars_matrix.plot.box(sym='r+')
mtcars_matrix.boxplot()
plt.savefig("boxplot.png")

# Determine which variable has the most impact on mpg.
mtcars_sub = mtcars.iloc[:, 1:]

# Determine which variable has the most impact on mpg.
# iterate through all columns and draw scatterplot vs mpg
fig, ax = plt.subplots(4, 3, figsize=(8, 6))
for index, name in enumerate(mtcars_sub.columns, start = 1):
    plt.subplot(4, 3, index, )
    plt.scatter(mtcars_sub[name], mtcars_sub["mpg"], s = 10)
    corr = mtcars_sub[name].corr(mtcars_sub["mpg"])
    plt.title(f'correlation: {corr:.3f}')
    plt.ylabel("mpg")
    plt.xlabel(name)

plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
plt.savefig("mpg-most-relevant.png")
