import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    fi_line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    y1 = np.arange(df['Year'].min(), 2051, 1)
    sl1 = y1 * fi_line.slope + fi_line.intercept
    plt.plot(y1, sl1)

    # Create second line of best fit
    df_2000 = df[df['Year'] > 1999]
    se_line = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    y2 = np.arange(df_2000['Year'].min(), 2051, 1)
    sl2 = y2 * se_line.slope + se_line.intercept
    plt.plot(y2, sl2)

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()