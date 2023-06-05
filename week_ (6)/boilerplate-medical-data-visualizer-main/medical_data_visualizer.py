import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df['weight'] / (df['height'] / 100) ** 2
df.overweight[df['overweight'] <= 25] = 0
df.overweight[df['overweight'] > 25] = 1

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.cholesterol[df['cholesterol'] == 1] = 0
df.cholesterol[df['cholesterol'] > 1] = 1
df.gluc[df['gluc'] == 1] = 0
df.gluc[df['gluc'] > 1] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat =  df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(data = df_cat, kind = "count",  x = "variable", hue = "value", col = "cardio").set(xlabel = 'variable', ylabel = 'total')


    # Get the figure for the output
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
    mask = mask = np.triu(np.ones_like(corr, dtype = bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (12, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask = mask, vmin = -0.16, vmax = 0.32, center = 0, square = True, linewidths = .5, annot = True, fmt = '.1f', ax = ax, cbar_kws = {'ticks': [-0.08, 0.00, 0.08, 0.16, 0.24], "shrink": 0.5})
    fig.savefig('heatmap.png')
    return fig

    
    
    
