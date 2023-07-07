import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    fig, ax = plt.subplots(figsize=(6,6))
    ax = plt.scatter(x, y)


    # Create first line of best fit
    slope, intercept, r_value, p_value, stderr = linregress(x, y)
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = slope*x_pred + intercept
    plt.plot(x_pred, y_pred, 'r')

  
    # Create second line of best fit
    df_forecast = df.loc[df['Year'] >= 2000]
    x_forecast = df_forecast['Year']
    y_forecast = df_forecast['CSIRO Adjusted Sea Level']

    # get new slope + intercept
    slope, intercept, r_value, p_value, stderr = linregress(x_forecast, y_forecast)
    x_pred2 = pd.Series([i for i in range(2000, 2051)])
    y_pred2 = slope*x_pred2 + intercept
    plt.plot(x_pred2, y_pred2, 'green')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year', fontsize = 12)
    plt.ylabel('Sea Level (inches)', fontsize = 12)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()