import pandas as pd

data = pd.read_csv("dataset.csv")
# Preview the first 5 lines of the loaded data
for i in data.columns:
    print(i)
