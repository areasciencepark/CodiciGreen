# This is a basic test
# to check that the algorithm actually drops empty lines
import pandas as pd 
 
raw_data = pd.read_excel("test_data_1.xlsx", dtype=str)
raw_data = raw_data[[ "IPC"]]
assert len(raw_data) == 4

raw_data.dropna(inplace=True)

assert len(raw_data) == 3
print("Test passed :-D")