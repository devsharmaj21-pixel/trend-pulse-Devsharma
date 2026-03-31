import pandas as pd
import numpy as np
import os

def analyze_data():
    if os.path.exists('data/processed_data.csv'):
        df = pd.read_csv('data/processed_data.csv')
        scores = np.array(df['score'])
        
        # Adding 2 Columns
        df['score_diff'] = scores - np.mean(scores)
        df['popularity'] = df['score'] + df['num_comments']
        df.to_csv('data/analyzed_data.csv', index=False)
        
        # Saving Results to Text File (The part I missed)
        if not os.path.exists('outputs'): os.makedirs('outputs')
        with open('outputs/analysis_results.txt', 'w') as f:
            f.write(f"--- Data Analysis Report ---\n")
            f.write(f"Total Posts: {len(df)}\n")
            f.write(f"Average Score: {np.mean(scores):.2f}\n")
            f.write(f"Highest Score: {np.max(scores)}\n")
            f.write(f"Top Post: {df.loc[df['score'].idxmax(), 'title']}\n")
        
        print("Task 3 Complete: Analyzed with NumPy & results saved to TXT.")
    else:
        print("Error: CSV not found.")

if __name__ == "__main__":
    analyze_data()