import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col = 'date', parse_dates = ['date'])

# Clean data
df = df[(df['value'] <= df['value'].quantile(0.975)) & (df['value'] >= df['value'].quantile(0.025))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(df.index, df['value'], 'r')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
     # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month_name()
    df_bar['month_name'] = df_bar.index.month
    df_bar = df_bar.groupby(['Year', 'Month']).mean().reset_index().sort_values(['month_name'])

    # Draw bar plot
    fig = plt.figure(figsize=(10,8))
    sns.barplot(data=df_bar, x='Year', y='value', hue='Month', palette='tab10')
    plt.legend(loc = 'upper left', title='Months')
    plt.ylabel('Average Page Views')
    plt.xlabel('Years')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['monum'] = df_box['date'].dt.month
    df_box = df_box.sort_values('monum')

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(ncols=2, figsize=(15,5))
    
    sns.boxplot(ax=ax[0], x='year', y='value', data=df_box).set(xlabel="Year", ylabel="Page Views", title="Year-wise Box Plot (Trend)")
    sns.boxplot(ax=ax[1], x='month', y='value', data=df_box ).set(xlabel="Month", ylabel="Page Views", title="Month-wise Box Plot (Seasonality)")


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
