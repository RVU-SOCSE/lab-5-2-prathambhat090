import csv
import pandas as pd
# create a csv file wtih random data and then data frame from csv file
with open('sample_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 25, 'New York'])
    writer.writerow(['Bob', 30, 'Los Angeles'])
    writer.writerow(['Charlie', 35, 'Chicago'])
    writer.writerow(['David', 40, 'Houston'])
    writer.writerow(['Eve', 45, 'Phoenix'])
df = pd.read_csv("sample_data.csv")
print("DataFrame from CSV:")
print(df)
print("Dimensions of the DataFrame:", df.shape)
print("Head of the DataFrame:")
print(df.head())
print("Tail of the DataFrame:")
print(df.tail())
print("Index of the DataFrame:", df.index)
print("Columns of the DataFrame:", df.columns)
print("Data types of the columns:")
print(df.dtypes) 