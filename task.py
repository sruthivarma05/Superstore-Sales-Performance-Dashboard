import pandas as pd
file_path = r"C:\Users\sruthi\Pictures\Downloads\New folder (7)\Sample - Superstore.xls"
data = pd.read_excel(file_path)
print(data.head())

#Data Cleaning Script

import pandas as pd

#Loading the dataset
file_path = r"C:\Users\sruthi\Pictures\Downloads\New folder (7)\Sample - Superstore.xls"
df = pd.read_excel(file_path)

#Showing initial info
print("Data Loaded Successfully!")
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())

#Removing duplicate rows
df.drop_duplicates(inplace=True)

#Handling missing values
# Fill missing postal codes with 0 (or leave blank if preferred)
df['Postal Code'] = df['Postal Code'].fillna(0)

# Droping rows with missing critical info
df.dropna(subset=['Sales', 'Profit', 'Quantity'], inplace=True)

#Converting dates to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

#Adding new columns for analysis
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month_name()
df['Order Month'] = df['Order Date'].dt.to_period('M')

#Creating a Profit Margin column
df['Profit Margin (%)'] = (df['Profit'] / df['Sales']) * 100

#Final clean-up
df = df.reset_index(drop=True)

print("\nData cleaned successfully!")
print("Shape after cleaning:", df.shape)
print("\nPreview:")
print(df.head())

#Saving cleaned data for dashboard use
df.to_csv("cleaned_superstore.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_superstore.csv'")
