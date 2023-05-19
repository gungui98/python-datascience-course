import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    line = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"], alternative='two-sided')
    plt.axline((df["Year"].min(), df["Year"].min() * line.slope + line.intercept), (2050, 2050 * line.slope + line.intercept), color="red")

    # Create second line of best fit
    line_2000 = linregress(x=df.loc[df["Year"] >= 2000, "Year"], y=df.loc[df["Year"] >= 2000, "CSIRO Adjusted Sea Level"], alternative='two-sided')
    plt.axline((2000, 2000 * line_2000.slope + line_2000.intercept), (2050, 2050 * line_2000.slope + line_2000.intercept), color="red")


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()