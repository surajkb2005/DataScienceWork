import pandas as pd

df = pd.read_csv("./sales_data_sample.csv")

print("First 5 rows: ",df.head(5))

#total sales

print("Total sales: ",df['SALES'].sum())

#best seller

bestProd = df.groupby("ORDERNUMBER")['QUANTITYORDERED'].sum().idxmax()
print("Best product ordernumber: ",bestProd)