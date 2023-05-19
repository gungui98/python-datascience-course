import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x = df['Year'], y = df['CSIRO Adjusted Sea Level'], color = 'darkviolet')

    # Create first line of best fit
    lineA = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    yearA = np.arange(df['Year'].min(), 2050, 1)
    sea_levelA = yearA * lineA.slope + lineA.intercept
    plt.plot(yearA, sea_levelA, color = 'khaki')

    # Create second line of best fit
    df_21st = df[df['Year'] > 1999]
    lineB = linregress(df_21st['Year'], df_21st['CSIRO Adjusted Sea Level'])
    yearB = np.arange(df_21st['Year'].min(), 2050, 1)
    sea_levelB = yearB * lineB.slope + lineB.intercept
    plt.plot(yearB, sea_levelB, color = 'turquoise')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()