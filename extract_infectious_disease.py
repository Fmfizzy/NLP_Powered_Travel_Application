import pandas as pd

excel_file_path = 'Tests/2023_contagious_disease_data.xlsx'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Extract columns 'start_week' and 'Total_weekly_disease'
columns_1 = ['start_week', 'Total_weekly_disease']
df1 = df[columns_1]

# Extract columns 'Disease_density' and 'location'
columns_2 = ['Disease_density', 'location']
df2 = df[columns_2]

# Print the extracted dataframes
print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)