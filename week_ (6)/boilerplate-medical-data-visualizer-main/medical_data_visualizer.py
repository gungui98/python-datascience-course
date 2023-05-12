import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = ((df['weight'] /
                     ((df['height'] / 100)**2)) > 25.0).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# Draw Categorical Plot
def draw_cat_plot():
  # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  lis = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
  df_cat = df.loc[:, [
    'id', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight',
    'cardio'
  ]]
  df_cat.head()
  df_cat = pd.melt(df_cat, id_vars='cardio', value_vars=lis)
  #print("df_cat", df_cat.head())
  # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
  g = sns.catplot(data=df_cat,
                    x='variable',
                    hue='value',
                    col='cardio',
                    kind='count')
  g.set_xlabels('variable')
  g.set_ylabels('total')
  # Draw the catplot with 'sns.catplot()'

  # Get the figure for the output
  fig = g.fig
  # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig


# Draw Heat Map
def draw_heat_map():
  # Clean the data
  df_heat = df.loc[(df['ap_lo'] <= df['ap_hi'])
                   & (df['height'] >= df['height'].quantile(0.025)) &
                   (df['height'] <= df['height'].quantile(0.975)) &
                   (df['weight'] >= df['weight'].quantile(0.025)) &
                   (df['weight'] <= df['weight'].quantile(0.975))]

  # Calculate the correlation matrix
  corr = df_heat.corr()
  mask = np.triu(np.ones_like(corr, dtype=bool))
  fig, ax0 = plt.subplots()

  # Draw the heatmap with 'sns.heatmap()'
  sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', ax=ax0)

  # Do not modify the next two lines
  fig.savefig('heatmap.png')
  return fig


if __name__ == '__main__':
  draw_cat_plot()
  draw_heat_map()
