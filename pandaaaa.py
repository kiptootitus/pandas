import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

print(pd.__version__)


# pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
# pandas series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.).

# Create a Pandas Series from List
 
a = [1, 7, 2]
 
myvar = pd.Series(a, index = ["x", "y", "z"])
 
print(myvar)


# pandas Dataframe is 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

data ={
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
  
}

# Load data into a DataFrame object:
df=pd.DataFrame(data)

print(df)

#creating a dataframe from a list of data

data ={
  'Name' : ['John', 'Anna', 'Peter', 'Linda'],
  'Age': [24, 13, 53, 33],
  'Address': ['California', 'Texas', 'Washington', 'Lousiana'],
  'Qualification': ['Msc', 'MA', 'Msc', 'Phd']
  
}
df=pd.DataFrame(data)

print(df)

#retriving data from a dataframe

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name")
 
# retrieving row by loc method
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]
 
 
print(first, "\n\n\n", second)


first = data['Age']

print(first)


dd = pd.read_csv('nba.csv')
 
print(dd.head())

print(dd.tail())