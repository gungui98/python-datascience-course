import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    line1 = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    x = pd.concat([df['Year'], pd.Series(np.arange(2014, 2051))])
    plt.plot(x, line1.intercept + line1.slope*x, 'r')

    # Create second line of best fit
    line2 = linregress(x=df.loc[df['Year'] >= 2000]['Year'], y=df.loc[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    x = pd.concat([df.loc[df['Year'] >= 2000]['Year'], pd.Series(np.arange(2014, 2051))])
    plt.plot(x, line2.intercept + line2.slope*x, 'r')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()