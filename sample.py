import pandas as pd


dataframe = pd.read_excel("Ertiga 1.4 Generation I NOT COMPLETED.xlsx",sheet_name="Sheet1")

data = dataframe[(dataframe["Km(x1000)"]==5)  ]
print(data.columns)