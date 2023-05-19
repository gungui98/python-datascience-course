import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    sns.scatterplot(data = df, x = 'Year', y = 'CSIRO Adjusted Sea Level', label = 'Real Sea Level') 
	

    # Create first line of best fit
    first = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = np.arange(df['Year'].min(), 2051, 1)
    y1 = first.slope * x1 + first.intercept
    
    df_first = pd.DataFrame({'Year' : x1, 'Predict Sea Level' : y1})
    sns.lineplot(data = df_first, x = 'Year', y = 'Predict Sea Level', color = 'red', label = 'Predict first')


    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    
    second = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x2 = np.arange(df_2000['Year'].min(), 2051, 1)
    y2 = second.slope * x2 + second.intercept
    
    df_second = pd.DataFrame({'Year' : x2, 'Predict Sea Level' : y2})
    p = sns.lineplot(data = df_second, x = 'Year', y = 'Predict Sea Level', color = 'g', label = 'Predict second')
    p.set_title('Rise in Sea Level')
    p.set_ylabel('Sea Level (inches)')


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()