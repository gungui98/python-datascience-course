import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=[0], index_col=0)

# Clean data
df = df.loc[(df.value >= df.value.quantile(0.025)) & (df.value <= df.value.quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(20,10))
    sns.lineplot(x='date', y = 'value', data=df, c='r')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month_name()
    df_bar['month_numbers'] = df_bar.index.month
    df_bar = df_bar.groupby(['Year', 'Month']).mean().reset_index().sort_values(['month_numbers'])

    # Draw bar plot
    fig = plt.figure(figsize=(5,10))
    sns.barplot(x='Year', y='value', hue='Month', data=df_bar)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.title('Months')
  
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box['Year'] = df_box.index.year
    df_box['Month'] = df_box.index.month_name()
    df_box['month_numbers'] = df_box.index.month
    df_box.sort_values('month_numbers', inplace=True)
    df_box.rename(columns={'value':'Page Views'}, inplace=True)

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(18,6))
    sns.boxplot(data=df_box, x='Year', y='Page Views', ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    
    sns.boxplot(data=df_box, x='Month', y='Page Views', ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xticklabels(labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
