
import pandas as pd 
  
raw_data = pd.read_excel("test_data_1.xlsx", dtype=str)
raw_data = raw_data[[ "IPC"]]

raw_data.dropna(inplace=True)
print(len(raw_data)) #expected value: 3

