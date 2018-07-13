from sklearn import tree
import numpy as np
import pandas as pd

input_file = "output.csv"


# comma delimited is the default
df = np.loadtxt(input_file, delimiter=",")

features = df[:, 0:1]  # select columns 1 through end
label = df[:, 2]   # select column 0, the stock price

original_headers = list(df.columns.values)

# remove the non-numeric columns
#df = df._get_numeric_data()

# put the numeric column names in a python list
#numeric_headers = list(df.columns.values)

# create a numpy array with the numeric values for input into scikit-learn
numpy_array = df.as_matrix()

# reverse the order of the columns
numeric_headers.reverse()
reverse_df = df[numeric_headers]

# write the reverse_df to an excel spreadsheet
reverse_df.to_excel('path_to_file.xls')