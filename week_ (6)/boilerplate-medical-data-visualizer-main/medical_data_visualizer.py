import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = df['weight'] / ((df['height'] / 100) ** 2)
df.loc[(df['overweight'] <= 25), 'overweight'] = 0
df.loc[(df['overweight'] > 25), 'overweight'] = 1
df['overweight'] = df['overweight'].astype(np.int64)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[(df['cholesterol'] <= 1), 'cholesterol'] = 0
df.loc[(df['gluc'] <= 1 ), 'gluc'] = 0
df.loc[ (df['cholesterol'] > 1 ), 'cholesterol'] = 1
df.loc[ (df['gluc']  > 1) , 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    
    

    # Draw the catplot with 'sns.catplot()'



    # Get the figure for the output
    
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'cholesterol', 'smoke', 'gluc', 'alco', 'overweight'])
    df_cat2 = df_cat.groupby(['cardio', 'variable', 'value'], as_index= False)
    df_cat = df_cat2.agg(total = pd.NamedAgg(column='value', aggfunc='count')) 

    graph = sns.catplot(data= df_cat, x = 'variable', y = 'total', col='cardio', hue='value', kind='bar')
    fig = graph.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
  
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]
    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask1 = np.ones(corr.shape)
    mask1 = np.triu(mask1)
    mask1 = mask1.astype(bool)



    # Set up the matplotlib figure
  
    fig, ax = plt.subplots(figsize=(16,9))
    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(data=corr, annot=True, fmt='0.1f', mask=mask1)
    

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
