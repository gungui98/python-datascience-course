import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    df.plot(kind = 'scatter', x = 'Year', y = 'CSIRO Adjusted Sea Level')  
    
    # Create first line of best fit
    #get the slope and y intercept 
    slope, y_int, r_val, p_val, std_err = linregress(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])
    #create the extra years
    extra_years = np.arange(2014, 2050)
    #convert the array to a Series
    extra_years = pd.Series(extra_years)
    #get the x value
    x = df['Year']
    #get the x for the linear plot
    futX = x.append(extra_years)
    
    #plot the linear plot of futX and y given mx + b
    plt.plot(futX, slope*futX + y_int)
    #set the labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches')
    plt.title('Rise in Sea Level')

    # Create second line of best fit
    #create a new df that is only the data from 2000 onwards
    modern = df.loc[df['Year'] >= 2000]
    #get the new slop and y intercept
    modSlope, mody_int, r_val, p_val, std_err = linregress(x = modern['Year'], y = modern ['CSIRO Adjusted Sea Level'])

    #get the x for the second scatter plot
    x2 = modern['Year']
    #get the futX based on the additional years needed
    futX2 = x2.append(extra_years)

    #plot the line of best fit
    plt.plot(futX2, modSlope * futX2 + mody_int)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()