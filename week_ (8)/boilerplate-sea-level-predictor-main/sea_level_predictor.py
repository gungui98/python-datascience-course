import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv("epa-sea-level.csv", float_precision="legacy")

    # Create scatter plot
    plt.figure(1, figsize=(16, 9))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    line = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    last_year = df["Year"].max()+1
    value = df['Year'] 
    value = pd.concat([value, pd.Series([y for y in range(last_year, 2051)])], axis=0)
    plt.plot(value,line.intercept + line.slope *value)

    # Create second line of best fit
    df = df.loc[(df["Year"] >= 2000)]
    value = value[value>=2000]
    line = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    plt.plot(value,line.intercept + line.slope * value)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()