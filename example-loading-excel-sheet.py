import pandas as pd

# Define the location of the file name
filename = 'C:/Users/Connie/Downloads/comparison.xlsx'

# Pick the sheet name you want to load into a pandas dataframe
df = pd.read_excel(filename, sheet_name="SheetNameGoesHere")

# Print the first five rows that are loaded
print(df.head(5))
