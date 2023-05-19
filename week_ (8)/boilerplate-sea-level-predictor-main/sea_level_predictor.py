import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

  # Create scatter plot
  plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c='b')
    
  #Create first line of best fit
  line1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  plt.plot(np.arange(1880, 2051), line1.intercept + line1.slope * np.arange(1880, 2051), 'r')

  #Create second line of best fit
  line2 = linregress(df.loc[df.Year >= 2000].Year, df.loc[df.Year >= 2000]['CSIRO Adjusted Sea Level'])
  plt.plot(np.arange(2000, 2051), line2.intercept + line2.slope * np.arange(2000, 2051), 'y')
  
  #Add labels and title
  plt.title('Rise in Sea Level')
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
