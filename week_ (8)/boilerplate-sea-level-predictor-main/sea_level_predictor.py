import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

  # Create scatter plot
  plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')

  # Create first line of best fit
  first = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  x1 = np.arange(df['Year'].min(), 2051, 1)
  y1 = first.slope * x1 + first.intercept

  plt.plot(x1, y1, 'red')

  # Create second line of best fit
  df_sec = df[df['Year'] >= 2000]
  second = linregress(df_sec['Year'], df_sec['CSIRO Adjusted Sea Level'])
  x2 = np.arange(df_sec['Year'].min(), 2051, 1)
  y2 = second.slope * x2 + second.intercept

  plt.plot(x2, y2, 'red')

  # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
