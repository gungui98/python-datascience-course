import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df['weight'] / (df['height'] / 100) ** 2

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[(df['overweight'] <= 25), 'overweight'] = 0
df.loc[(df['overweight'] > 25), 'overweight'] = 1
df = df.astype({'overweight' : 'int64'})
df.loc[(df['cholesterol'] == 1), 'cholesterol'] = 0
df.loc[(df['cholesterol'] > 1), 'cholesterol'] = 1
df.loc[(df['gluc'] == 1), 'gluc'] = 0
df.loc[(df['gluc'] > 1), 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(data = df_cat, kind ='count', x = 'variable', hue = 'value', col = 'cardio')
    fig.set(xlabel = 'variable', ylabel = 'total')
    fig = fig.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True


    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, vmin = -0.16, vmax = 0.32, center = 0, square = True, fmt = '.1f', linewidths = .5, cbar_kws = {'ticks': np.arange(-0.08, 0.32, 0.08), "shrink": 0.5}, mask = mask, annot = True, ax = ax)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
