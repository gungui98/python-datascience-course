import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    first_line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = pd.concat([df['Year'], pd.Series(np.arange(2014, 2051))])
    plt.plot(x, first_line.intercept + first_line.slope*x)

    # Create second line of best fit
    df_2000 = df.loc[df['Year'] >= 2000]
    x = pd.concat([df_2000['Year'], pd.Series(np.arange(2014, 2051))])
    second_line = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    plt.plot(x, second_line.intercept + second_line.slope*x)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()