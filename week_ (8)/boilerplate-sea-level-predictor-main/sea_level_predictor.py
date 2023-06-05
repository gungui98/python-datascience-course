import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress


def draw_plot():
  # Read data from file
  df = pd.read_csv("epa-sea-level.csv")

  # Create scatter plot
  plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')

  def plot_linregress(df, color):
    slope, intercept, r_value, p_value, std_err = linregress(
      df['Year'], df['CSIRO Adjusted Sea Level'])
    xa = range(df['Year'].min(), 2051, 1)
    ya = xa * slope + intercept
    df_1 = pd.DataFrame({'Year': xa, 'Predict sea level': ya})
    sns.lineplot(data=df_1,
                 x='Year',
                 y='Predict sea level',
                 color=color,
                 label='Predict')

  # Create first line of best fit
  plot_linregress(df, 'g')

  # Create second line of best fit
  plot_linregress(df[df.Year >= 2000], 'r')

  # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
