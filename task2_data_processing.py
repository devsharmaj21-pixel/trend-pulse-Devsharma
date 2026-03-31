import pandas as pd
import json
import os

def process_data():
    print("--- Task 2: Processing CSV Data ---")
    
    # Requirement: Load the CSV file created in Task 1
    csv_path = 'data/raw_data.csv'
    
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        
        # Clean the data: drop duplicates, fill NaN with 0
        df = df[['title', 'score', 'num_comments']].drop_duplicates().fillna(0)
        
        # Requirement: Save as CSV
        output_path = 'data/processed_data.csv'
        df.to_csv(output_path, index=False)
        print(f"Success! Processed data saved to: {output_path}")
    else:
        print("Error: 'raw_data.csv' not found! Run Task 1 first.")

if __name__ == "__main__":
    process_data()