import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('/work/epa-sea-level.csv')
    x = df['CSIRO Adjusted Sea Level']
    y = df["Year"]
    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x, y)

    # Create first line of best fit
    res = linregress(x, y)
    x_prediction = pd.Series([i for i in range (1880, 2051)])
    y_prediction = res.slope*x_prediction + res.intercept
    plt.plot(x_prediction, y_prediction, "r")
    # Create second line of best fit
    new_df = df.loc[df['Year'] >= 2000]
    new_x = new_df['Year']
    new_y = new_df["CSIRO Adjusted Sea Level"]
    n_res = linregress(new_x, new_y)
    x_pred2 = pd.Series([i for i in range (2000,2051)])
    y_pred2 = n_res.slope*x_pred2 + n_res.intercept
    plt.plot(x_pred2, y_pred2, 'green')
    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()