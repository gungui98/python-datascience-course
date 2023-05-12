import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column

df['overweight'] = (df['weight'] / ((df['height'] / 100)**2) > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(by = ['cardio', 'variable', 'value'], as_index = False).size()
    df_cat = df_cat.rename(columns = {'size' : 'total'})
    

    # Draw the catplot with 'sns.catplot()'
	fig = sns.catplot(data = df_cat, x = 'variable', y = 'total', hue = 'value', col = 'cardio', kind = 'bar').fig


    


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    lowweight = df['weight'].quantile(0.025)
    highweight = df['weight'].quantile(0.975)
    lowheight = df['height'].quantile(0.025)
    highheight = df['height'].quantile(0.975)
    
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])& (df['weight'] <= highweight)& (df['weight'] >= lowweight)& (df['height'] <= highheight) & (df['height'] >= lowheight)]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype = bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (22, 20), dpi = 100)

    # Draw the heatmap with 'sns.heatmap()'
	sns.heatmap(corr, mask = mask, annot = True, fmt = '.1f')
	

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
