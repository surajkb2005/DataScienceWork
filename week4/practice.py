import pandas as pd
import matplotlib.pyplot as plt

# Make numeric output look nicer
pd.options.display.float_format = "{:,.2f}".format


# 1. BAR CHART – SALES BY PRODUCT CATEGORY

# Create example sales data
sales_data = {
    "Category": ["Electronics", "Clothing", "Groceries", "Toys", "Books"],
    "Sales":    [20000, 15000, 12000, 8000, 6000]
}
sales_df = pd.DataFrame(sales_data)

# Bar chart
plt.figure(figsize=(8, 5))
plt.bar(sales_df["Category"], sales_df["Sales"])
plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()


# 2. LINE CHART – MONTHLY TEMPERATURE CHANGES

# Create example temperature data
temp_data = {
    "Month":   ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "AvgTemp": [18, 20, 24, 28, 30, 32,
                33, 32, 29, 25, 21, 19]
}
temp_df = pd.DataFrame(temp_data)

# Ensure months are in correct order
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
temp_df["Month"] = pd.Categorical(temp_df["Month"],
                                  categories=month_order,
                                  ordered=True)
temp_df = temp_df.sort_values("Month")

# Line chart
plt.figure(figsize=(8, 5))
plt.plot(temp_df["Month"], temp_df["AvgTemp"], marker="o")
plt.title("Average Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True, linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.show()


# 3. PIE CHART – EXPENSE DISTRIBUTION

# Create example expense data
expense_data = {
    "Category": ["Rent", "Food", "Transport", "Entertainment", "Others"],
    "Amount":   [15000, 6000, 2000, 1500, 1000]
}
expense_df = pd.DataFrame(expense_data)

# Pie chart
plt.figure(figsize=(6, 6))
plt.pie(
    expense_df["Amount"],
    labels=expense_df["Category"],
    autopct="%1.1f%%",
    startangle=90,
)
plt.title("Expense Distribution by Category")
plt.tight_layout()
plt.show()