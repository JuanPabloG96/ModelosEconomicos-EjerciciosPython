import pandas as pd 

file_path = "src/datasets/peces_dataset.xlsx"
data = pd.read_excel(file_path, sheet_name=0)

print(data.head())
