import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(14,6))
    ax.plot(df.index, df['value'], c='r', linewidth=1)
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Years'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month_name()
    df_bar['month_number'] = df_bar.index.month
    df_bar = df_bar.groupby(['Years', 'Month']).mean().reset_index().sort_values(['month_number'])
    df_bar.rename(columns = {'value': 'Average Page Views'}, inplace = True)

    # Draw bar plot
    fig = plt.figure(figsize=(10,15))
    barplot = sns.barplot(data=df_bar, x = 'Years', hue = 'Month', y = 'Average Page Views')
    plt.title('Month')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15,6))

    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[0].set_title('Year-wise Box Plot (Trend)')

    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x='month', y='value', data=df_box, order=months_order, ax=axes[1])
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
