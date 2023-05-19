import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(1, 1, figsize = (10, 10))
    ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    linOriginal = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = np.arange(df['Year'].min(), 2050, 1)
    y1 = linOriginal.slope * x1 + linOriginal.intercept
    ax.plot(x1, y1, 'r')

    # Create second line of best fit
    df2000 = df.loc[df['Year'] > 2000]
    lin2000 = linregress(df2000['Year'], df2000['CSIRO Adjusted Sea Level'])
    x2 = np.arange(2000, 2050, 1)
    y2 = lin2000.slope * x2 + lin2000.intercept
    ax.plot(x2, y2, 'b')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()