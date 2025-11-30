import pandas as pd

#loading few dataset
df = pd.read_csv("./StudentsPerformance.csv")

#printin 5 rows
print(df.head(5))

#Number of rows and columns
print("(rows,columns) : ",df.shape)

#datatypes
print(df.dtypes)

#missing values
print("Missing values (before): ",df.isnull().sum())

#handling missing values
m_mathscore = df['math score'].mean()
m_readingscore = df['reading score'].mean()
m_writingscore = df['writing score'].mean()

df['math score'] = df['math score'].fillna(m_mathscore)
df['reading score'] = df['reading score'].fillna(m_readingscore)
df['writing score'] = df['writing score'].fillna(m_writingscore)

print("Missing values (after): ",df.isnull().sum())


#statistical
print("Average math score : ",df['math score'].mean())
print("Lowest reading score: ",df['reading score'].min())
print("Highest writing score: ",df['writing score'].max())