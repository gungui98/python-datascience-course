import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    x1 = range(df['Year'].iloc[0], 2051, 1)
    first_line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(x1, first_line.intercept + x1 * first_line.slope, 'r', label='Best Fit Line')

    # Create second line of best fit
    recent_years_df = df[df['Year'] >= 2000]
    x2 = range(2000, 2051, 1)
    second_line = linregress(recent_years_df['Year'], recent_years_df['CSIRO Adjusted Sea Level'])
    plt.plot(x2, second_line.intercept + second_line.slope * x2, 'g', label='Best Fit Line - Recent')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend() 
    plt.xlim(1850, 2075) 
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()