
import pandas as pd
data = pd.Series([10, 20, 30, 40, 50], index = ['a', 'b', 'c', 'd', 'e'])
students = pd.Series([85, 90, 78, 92, 88],
                        index = ['Alice', 'Bob', 'Charlie', 'David', 'Eve'])
print(data)
print(students)

# Accessing elements in the series
print(data['c']) 
print(students['Alice'])  
print(data + 5)  
print(students * 2)  

# Filtering the series
print(data[data > 25]) 
print(students[students >= 90])

#statistics
print(data.mean())
print(students.mean())

#head and tail 
print(data.head(3))
print(students.tail(2))

# accesing column
data = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
                     'Age': [25, 30, 35, 40, 45],
                     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']})
print(data['Name'])
print(data['Age'])
print(data['City'])


#accessing row
print(data.loc[0])
print(data.loc[1])
print(data.loc[2])
print(data.loc[3])

#null elements 
data = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
                     'Age': [25, 30, None, 40, 45],
                     'City': ['New York', 'Los Angeles', 'Chicago', None, 'Phoenix']})
print(data)
print(data.isnull())
print(data.notnull())
print(data.dropna())

#filling null values
print(data.fillna({'Age': data['Age'].mean(), 'City': 'Unknown'}))

#
