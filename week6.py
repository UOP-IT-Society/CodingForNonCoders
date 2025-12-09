import pandas as pd
import numpy as np

# ==========================================
# 0. DATA SETUP (Run this to make examples work)
# ==========================================
# Main DataFrame used in most examples
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, np.nan], # Includes a null for cleaning examples
    'City': ['NY', 'LA', 'NY', 'sf', 'LA'], 
    'Salary': [70000, 80000, 120000, 90000, 60000],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023/01/04', '2023-01-05'],
    'Price': ['100', '200', '300', '400', '500'], # String format for type conversion
    'Industry': ['Tech', 'Finance', 'Tech', 'Healthcare', 'Finance']
}
df = pd.DataFrame(data_dict)

# DataFrames for Merging Slide
orders = pd.DataFrame({
    'order_id': [1, 2, 3], 
    'customer_id': [101, 102, 103], 
    'amount': [250, 150, 300]
})
customers = pd.DataFrame({
    'customer_id': [101, 102], 
    'name': ['Alice', 'Bob']
})

# ==========================================
# SLIDE 4: Installation & Setup
# ==========================================
print(pd.__version__)

# ==========================================
# SLIDE 6: Creating a Series
# ==========================================
# From a List
s = pd.Series([10, 20, 30])

# From a Dictionary
data_s = {'a': 10, 'b': 20}
s_dict = pd.Series(data_s)
print(s_dict)

# ==========================================
# SLIDE 7: Series Attributes
# ==========================================
s = pd.Series([10, 20, 30], index=['x', 'y', 'z'])
print(s.index)   # Index(['x', 'y', 'z'])
print(s.values)  # [10 20 30]
print(s.dtype)   # int64
print(s.shape)   # (3,)

# ==========================================
# SLIDE 8: Indexing & Slicing
# ==========================================
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s['a'])    # By Label: 10
print(s[0])      # By Position: 10
print(s[:2])     # Slicing: a and b

# ==========================================
# SLIDE 9: Vectorized Operations
# ==========================================
prices = pd.Series([100, 200, 300])
total = prices * 1.1            # Add Tax (10%)
high_cost = prices[prices > 150] # Filter

# ==========================================
# SLIDE 13: Inspecting Data
# ==========================================
print(df.head())
print(df.info())
print(df.describe())
print(df.shape)

# ==========================================
# SLIDE 14: Selecting Columns
# ==========================================
ages = df['Age']              # Series
ages_dot = df.Age             # Series (dot notation)
subset = df[['Name', 'City']] # DataFrame

# ==========================================
# SLIDE 15: Row Selection (loc vs iloc)
# ==========================================
# Note: Setting 'Name' as index temporarily to demonstrate loc
df_indexed = df.set_index('Name')

# loc (Label based)
row_loc = df_indexed.loc['Alice']

# iloc (Position based)
row_iloc = df.iloc[0]
rows_slice = df.iloc[0:5]

# ==========================================
# SLIDE 16: Filtering Data
# ==========================================
mask = df['Age'] > 25
adults = df[mask]

# One-liner
nyc_residents = df[df['City'] == 'NY']

# ==========================================
# SLIDE 21: Date Parsing
# ==========================================


# Convert string to datetime
df['Date'] = pd.to_datetime(df['Date'],format='%Y-%m-%d', errors='coerce')
print(df['Date'].dt.year)   # Extract Year
print(df['Date'].dt.month)  # Extract Month
print(df['Date'].dt.day)    # Extract Day

# ==========================================
# SLIDE 22: Handling Nulls
# ==========================================
clean = df.dropna()              # Drop rows with nulls
filled = df.fillna(0)            # Fill nulls with 0
# Fill with Mean
mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age) # Assign back to column

# ==========================================
# SLIDE 23: Renaming Columns
# ==========================================
df.rename(columns={
    'Salary': 'Annual_Salary'
}, inplace=True)

# ==========================================
# SLIDE 24: Type Conversion
# ==========================================
df['Price'] = df['Price'].astype(float)

# ==========================================
# SLIDE 26: String Operations
# ==========================================
df['Name'] = df['Name'].str.upper()
tech_cos = df[df['Industry'].str.contains('Tech')]

# ==========================================
# SLIDE 27: Sorting
# ==========================================
sorted_df = df.sort_values(by='Annual_Salary', ascending=False)

# ==========================================
# SLIDE 28: GroupBy
# ==========================================
# Avg Salary by Industry
print(df.groupby('Industry')['Annual_Salary'].mean())

# Count by City
print(df.groupby('City').size())

# ==========================================
# SLIDE 29: Merging
# ==========================================
merged = pd.merge(
    orders, 
    customers, 
    on='customer_id', 
    how='left'
)
print(merged)

# ==========================================
# SLIDE 30: Pivot Tables
# ==========================================
# Creating a dummy 'Sales' column for the pivot example
df['Sales'] = [100, 200, 150, 300, 250]

table = pd.pivot_table(
    df, 
    values='Sales', 
    index='City', 
    columns='Industry', 
    aggfunc='sum'
)
print(table)