import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    year = pd.concat([df.Year, pd.Series(range(df.Year.iloc[-1]+1,2051))],ignore_index = True)
    # Create scatter plot
    plt.scatter(data = df, x = 'Year', y = 'CSIRO Adjusted Sea Level')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x = df.Year, y = df['CSIRO Adjusted Sea Level'])
    plt.plot(year,year*slope + intercept, color = 'red')
    # Create second line of best fit
    df_2000 = df[df.Year >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(x = df_2000.Year, y = df_2000['CSIRO Adjusted Sea Level'])
    plt.plot(year[year>=2000],year[year>=2000]*slope + intercept, color = 'green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()