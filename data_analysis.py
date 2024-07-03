import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv('sales_data_sample.csv', encoding='Windows-1252')
data['ORDERDATE'] = pd.to_datetime(data['ORDERDATE'], errors='coerce')
data['TotalSales'] = data['SALES']
missing_values = data.isnull().sum()
missing_values, data.dtypes

# Extract quarter, month, and year from ORDERDATE
data['QUARTER'] = data['ORDERDATE'].dt.quarter
data['MONTH'] = data['ORDERDATE'].dt.month
data['YEAR'] = data['ORDERDATE'].dt.year

# Calculate total sales per quarter, month, and year
sales_per_quarter = data.groupby(['YEAR', 'QUARTER'])['TotalSales'].sum().reset_index()
sales_per_month = data.groupby(['YEAR', 'MONTH'])['TotalSales'].sum().reset_index()
sales_per_year = data.groupby('YEAR')['TotalSales'].sum().reset_index()

# Plotting total sales per quarter
plt.figure(figsize=(10, 6))
plt.plot(sales_per_quarter['YEAR'].astype(str) + '-Q' + sales_per_quarter['QUARTER'].astype(str), sales_per_quarter['TotalSales'], marker='o')
plt.title('Total Sales per Quarter')
plt.xlabel('Quarter')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Plotting total sales per month
plt.figure(figsize=(10, 6))
plt.plot(sales_per_month['YEAR'].astype(str) + '-' + sales_per_month['MONTH'].astype(str).str.zfill(2), sales_per_month['TotalSales'], marker='o')
plt.title('Total Sales per Month')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=90)
plt.grid(True)
plt.show()

# Plotting total sales per year
plt.figure(figsize=(10, 6))
plt.bar(sales_per_year['YEAR'].astype(str), sales_per_year['TotalSales'])
plt.title('Total Sales per Year')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# Top 10 products by total sales
top_products = data.groupby('PRODUCTCODE')['TotalSales'].sum().sort_values(ascending=False).head(10).reset_index()

# Top-performing product lines
top_product_lines = data.groupby('PRODUCTLINE')['TotalSales'].sum().sort_values(ascending=False).reset_index()

# Plotting top 10 products by total sales
plt.figure(figsize=(12, 6))
plt.barh(top_products['PRODUCTCODE'], top_products['TotalSales'], color='skyblue')
plt.title('Top 10 Products by Total Sales')
plt.xlabel('Sales')
plt.ylabel('Product Code')
plt.gca().invert_yaxis()
plt.grid(True)
plt.show()

# Plotting top-performing product lines
plt.figure(figsize=(12, 6))
plt.barh(top_product_lines['PRODUCTLINE'], top_product_lines['TotalSales'], color='skyblue')
plt.title('Top-Performing Product Lines')
plt.xlabel('Sales')
plt.ylabel('Product Line')
plt.gca().invert_yaxis()
plt.grid(True)
plt.show()

# Display dataframes for inspection
print("Sales per Quarter:\n", sales_per_quarter)
print("Sales per Month:\n", sales_per_month)
print("Sales per Year:\n", sales_per_year)
print("Top 10 Products by Total Sales:\n", top_products)
print("Top-Performing Product Lines:\n", top_product_lines)
