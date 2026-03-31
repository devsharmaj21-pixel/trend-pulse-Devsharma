import pandas as pd
import matplotlib.pyplot as plt
import os

def create_visuals():
    print("--- Task 4: Creating 3 Different Charts ---")
    
    # Task 3 ki banayi file load karna
    input_file = 'data/analyzed_data.csv'
    
    if os.path.exists(input_file):
        df = pd.read_csv(input_file).head(10)
        
        if not os.path.exists('outputs'):
            os.makedirs('outputs')

        # 1. Bar Chart (Scores)
        plt.figure(figsize=(10, 5))
        plt.bar(df['title'].str[:15], df['score'], color='skyblue')
        plt.title("Post Scores Bar Chart")
        plt.xticks(rotation=45)
        plt.savefig('outputs/bar_chart.png')
        plt.close()

        # 2. Line Chart (Comments Trend)
        plt.figure(figsize=(10, 5))
        plt.plot(df['title'].str[:15], df['num_comments'], marker='o', color='red')
        plt.title("Comments Line Chart")
        plt.xticks(rotation=45)
        plt.savefig('outputs/line_chart.png')
        plt.close()

        # 3. Scatter Plot (Score vs Comments)
        plt.figure(figsize=(8, 6))
        plt.scatter(df['score'], df['num_comments'], color='green')
        plt.title("Score vs Comments Scatter Plot")
        plt.xlabel("Score")
        plt.ylabel("Comments")
        plt.savefig('outputs/scatter_plot.png')
        plt.close()

        print("Success! 3 charts (Bar, Line, Scatter) saved in 'outputs' folder.")
    else:
        print("Error: analyzed_data.csv not found!")

if __name__ == "__main__":
    create_visuals()
