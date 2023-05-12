import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = df= pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df['overweight']=(df['weight']/((df['height']/100)**2) > 25).replace({True: 1, False: 0})

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from
    # 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    vars = sorted(["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=vars,)

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot
    # to work correctly.
    df_cat = df_cat.value_counts().reset_index(name="total")

    # Draw the catplot with 'sns.catplot()'
    fig,ax = sns.catplot(data=df_cat, x="variable", y="total", hue="value", col="cardio", kind="bar")
    ax.set_ylabels("total")
    ax.set_xlabels("variable")

    # Do not modify the next two lines
    fig.savefig("catplot.png")
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.loc[(df["ap_lo"] <= df["ap_hi"]) & (df["height"] >= df["height"].quantile(0.025)) & (df["height"] <= df["height"].quantile(0.975))& (df["weight"] >= df["weight"].quantile(0.025))& (df["weight"] <= df["weight"].quantile(0.975))]

    # Calculate the correlation matrix
    corr= df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots()

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap( corr, mask=mask, vmax=0.4, square=True, fmt=".1f", annot=True)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
