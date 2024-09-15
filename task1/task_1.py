import pandas as pd
import sys

assert(len(sys.argv) == 4), f"Provide full path to csv, row and column"
print(sys.argv)

path_to_program, path_to_csv, row, column = sys.argv

data = pd.read_csv(path_to_csv, header=None, index_col=None)
print(data.iloc[int(row), int(column)])