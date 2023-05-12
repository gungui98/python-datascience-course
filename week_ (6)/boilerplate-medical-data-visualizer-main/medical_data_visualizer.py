import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
<<<<<<< HEAD
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['BMI'] = df['weight']/((df['height']**2)/10000)
df['overweight'] = 0
df.loc[df['BMI'] > 25,'overweight'] = 1


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df['cholesterol'] == 1,'cholesterol'] = 0
df.loc[df['cholesterol'] > 1,'cholesterol'] = 1
df.loc[df['gluc'] == 1,'gluc'] = 0
df.loc[df['gluc'] > 1,'gluc'] = 1
=======
df = None

# Add 'overweight' column
df['overweight'] = None

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

>>>>>>> 525d56702a5550e7e07345bed05263e073c0727f

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
<<<<<<< HEAD
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    df_cat = df_cat.rename(columns = {0:'total'})
=======
    df_cat = None


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = None
>>>>>>> 525d56702a5550e7e07345bed05263e073c0727f
    

    # Draw the catplot with 'sns.catplot()'

<<<<<<< HEAD
    graph = sns.catplot(data=df_cat, kind="bar", x="variable", y="total", hue="value", col="cardio")


    # Get the figure for the output
    fig = graph.fig
=======


    # Get the figure for the output
    fig = None
>>>>>>> 525d56702a5550e7e07345bed05263e073c0727f


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
<<<<<<< HEAD
    df_heat = df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))
            ]

    # Calculate the correlation matrix
    corr = corr = df_heat.corr()


    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

  # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(16, 9))

  # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, square=True, linewidths=0.5, annot=True, fmt="0.1f")
=======
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None
>>>>>>> 525d56702a5550e7e07345bed05263e073c0727f

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
