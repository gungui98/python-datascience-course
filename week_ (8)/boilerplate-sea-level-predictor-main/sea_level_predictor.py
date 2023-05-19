import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    fig = plt.figure()
    
    # Create scatter plot
    sns.scatterplot(data=df, x='Year', y='CSIRO Adjusted Sea Level')

    # Create first line of best fit
    slope, intercept, a, b, c = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    a = df['Year']
    b = pd.Series(range(2014, 2051))
    a = pd.concat([a, b])
    sns.lineplot(x=a, y=intercept + slope*a, c='r')

    # Create second line of best fit
    slope2, intercept2, a, b, c = linregress(df['Year'][df['Year']>=2000], df['CSIRO Adjusted Sea Level'][df['Year']>=2000])
    c = df['Year'][df['Year']>=2000]
    d = pd.Series(range(2014, 2051))
    c = pd.concat([c, d])
    sns.lineplot(x=c, y=intercept2 + slope2*c, c='orange')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    fig.savefig('sea_level_plot.png')
    return fig.gca()