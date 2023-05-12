import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = (df["weight"] / ((df["height"] / 100) ** 2) > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index()
    df_cat.columns = ['cardio', 'variable', 'value', 'total']

    # Draw the catplot with 'sns.catplot()'



    # Get the figure for the output
    g = sns.catplot(data=df_cat, x="variable", y="total", col="cardio", hue="value", kind="bar", height=8, aspect=1.2, errorbar=None)
    fig = g.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    condition1 = (df['ap_lo'] <= df['ap_hi'])
    condition2 = (df['height'] >= df['height'].quantile(0.025))
    condition3 = (df['height'] <= df['height'].quantile(1 - 0.025))
    condition4 = (df['weight'] >= df['weight'].quantile(0.025))
    condition5 = (df['weight'] <= df['weight'].quantile(1 - 0.025))
    df_heat = df.loc[condition1 & condition2 & condition3 & condition4 & condition5]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(32, 16))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask = mask, annot=True, linewidths=.5, fmt=".1f")


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig