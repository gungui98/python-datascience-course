import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.scatter(data = df, x = 'Year', y = 'CSIRO Adjusted Sea Level')

    # Create first line of best fit
    line1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x1 = range(df["Year"].iloc[0], 2051, 1)
    plt.plot(x1, line1.intercept + line1.slope*x1, 'r', label='fitted line 1')
    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    x2 = range(2000, 2051, 1)
    line2 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    plt.plot(x2, line2.intercept + line2.slope*x2, 'g', label='fitted line 2')
    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    plt.legend()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()