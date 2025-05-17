# Import pandas
import pandas as pd

# Load your dataset
df = pd.read_csv("sales_data.csv")

# Print first 5 rows to see what the data looks like
print(df.head())

# Basic info (column types, missing values, etc.)
print("\nDataset Info:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Display dataset
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Convert 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Total sales by category
print("\nTotal Sales by Category:")
print(df.groupby("Category")["Total Sales"].sum())

# Total sales by region
print("\nTotal Sales by Region:")
print(df.groupby("Region")["Total Sales"].sum())

# Best-selling products
print("\nBest-Selling Products:")
print(df.groupby("Product")["Total Sales"].sum().sort_values(ascending=False).head(3))

# Visualization: Total Sales by Region
region_sales = df.groupby("Region")["Total Sales"].sum()
region_sales.plot(kind="bar", title="Total Sales by Region", color="skyblue")
plt.ylabel("Total Sales")
plt.xlabel("Region")
plt.tight_layout()