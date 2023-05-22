import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_fi = np.arange(df['Year'].min(),2051,1)
    y_fi = result.slope*x_fi + result.intercept
    plt.plot(x_fi,y_fi)

    # Create second line of best fit
    df2000 = df[df['Year'] >= 2000]
    second = linregress(df2000["Year"], df2000['CSIRO Adjusted Sea Level'] )
    x_se = np.arange(2000, 2051, 1)
    y_se = second.intercept + x_se*second.slope
    plt.plot(x_se, y_se)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()