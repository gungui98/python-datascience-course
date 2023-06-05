import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    year = np.arange(df['Year'].min(), 2051, 1)
    plt.plot(year, year * line.slope + line.intercept)

    # Create second line of best fit
    df2 = df[df['Year'] > 1999]
    line2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    year2 = np.arange(df2['Year'].min(), 2051, 1)
    plt.plot(year2, year2 * line2.slope + line2.intercept)

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
