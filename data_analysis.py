import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

data = pd.read_csv('sales_data_sample.csv', encoding='Windows-1252')
data['ORDERDATE'] = pd.to_datetime(data['ORDERDATE'])
data['TotalSales'] = data['SALES']


def analyze_data(choice, data, order_number=None):
    if choice == 1:
        # Total sales by order number
        summary = data.groupby('ORDERNUMBER')['TotalSales'].sum().reset_index()
        fig = px.bar(summary, x='ORDERNUMBER', y='TotalSales', title='Total Sales by Order Number')
    elif choice == 2:
        # Sales over time (monthly)
        summary = data.groupby(data['ORDERDATE'].dt.to_period('M'))['TotalSales'].sum().reset_index()
        summary['ORDERDATE'] = summary['ORDERDATE'].dt.strftime('%Y-%m')
        fig = px.line(summary, x='ORDERDATE', y='TotalSales', title='Sales Over Time (Monthly)')
    elif choice == 3 and order_number is not None:
        # Performance of a specific order over time 
        print("Enter the ORDER NUMBER you want to analyze.")
        order_number = input("Enter the order number: ")
        specific_order_data = data[data['ORDERNUMBER'] == int(order_number)]
        if specific_order_data.empty:
            print("Order number not found.") 
            return
        summary = specific_order_data.groupby(specific_order_data['ORDERDATE'].dt.to_period('M'))['TotalSales'].sum().reset_index()
        summary['ORDERDATE'] = summary['ORDERDATE'].dt.strftime('%Y-%m')
        fig = px.line(summary, x='ORDERDATE', y='TotalSales', title=f'Sales Trend for Order {order_number}')
    elif choice == 4:
        # Seasonal Sales Analysis
        summary = data.groupby('MONTH_ID')['TotalSales'].sum().reset_index()
        fig = px.bar(summary, x='MONTH_ID', y='TotalSales', title='Seasonal Sales Analysis', labels={'MONTH_ID': 'Month', 'TotalSales': 'Total Sales'})
    else:
        print("Invalid choice. Please select a valid option.")
        return
    
    fig.show() 

# User interaction for selecting analysis type   
print("Select the type of analysis you'd like to perform:")
print("1. Total Sales by Order Number")
print("2. Sales Over Time (Monthly)")
print("3. Performance of a Specific Order Over Time")
print("4. Seasonal Sales Analysis")
print("5. Individual Sales Analysis")
choice = int(input("Enter your choice (1-4): "))
order_number = None
if choice == 3:
    order_number = int(input("Enter the order number: "))

# Perform the analysis
analyze_data(choice, data, order_number)