import pandas as pd
import numpy as np
import re

def clean_rate(rate):
    if pd.isna(rate) or rate == 'NEW' or rate == '-':
        return np.nan
    rate = str(rate).split('/')[0]
    try:
        return float(rate)
    except ValueError:
        return np.nan

def clean_cost(cost):
    if pd.isna(cost):
        return np.nan
    cost = str(cost).replace(',', '')
    try:
        return float(cost)
    except ValueError:
        return np.nan

def clean_data(input_file, output_file):
    print(f"Loading data from {input_file}...")
    df = pd.read_csv(input_file)
    
    # 1. Handle missing values for critical columns
    # We will drop rows where 'name' or 'address' are missing as they are identifiers
    df.dropna(subset=['name', 'address'], inplace=True)
    
    # 2. Clean numeric columns
    print("Cleaning 'rate' and 'approx_cost' columns...")
    df['rate'] = df['rate'].apply(clean_rate)
    df['approx_cost(for two people)'] = df['approx_cost(for two people)'].apply(clean_cost)
    
    # 3. Handle missing values in 'location' and 'rest_type'
    # Fill with 'Unknown' instead of dropping, unless too many are missing
    df['location'].fillna('Unknown', inplace=True)
    df['rest_type'].fillna('Unknown', inplace=True)
    
    # 4. Standardize online_order and book_table
    df['online_order'] = df['online_order'].map({'Yes': True, 'No': False})
    df['book_table'] = df['book_table'].map({'Yes': True, 'No': False})
    
    # 5. Remove duplicates
    print("Removing duplicates...")
    before_count = len(df)
    df.drop_duplicates(subset=['name', 'address'], inplace=True)
    after_count = len(df)
    print(f"Removed {before_count - after_count} duplicate rows.")
    
    # 6. Save cleaned data
    print(f"Saving cleaned data to {output_file}...")
    df.to_csv(output_file, index=False)
    print("Data cleaning complete.")

if __name__ == "__main__":
    input_csv = "round1.csv"
    output_csv = "cleaned_restaurant_data.csv"
    clean_data(input_csv, output_csv)
