import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates = [0], index_col = 0)

# Clean data
df = df[(df['value'] >= df.value.quantile(0.025)) & (df['value'] <= df.value.quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize = (15, 5))
    sns.lineplot(data = df, x = df.index, y = 'value', color = 'red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.show()
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month_name()
    
    # Draw bar plot
    fig = plt.figure(figsize = (10, 10))
    order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    handles = sns.barplot(data = df_bar, x = 'Year', hue = 'Month', y = 'value', ci = None, hue_order = order, palette = 'tab10')
    handles.set(xlabel = 'Years', ylabel = 'Average Page Views')
    plt.legend(title = 'Month', loc = "upper left")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [int(d.strftime('%m')) for d in df_box.date]
    df_box = df_box.sort_values('month')
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2)
    fig.set_size_inches(15, 5)
    sns.boxplot(data = df_box, x = 'year', y = 'value', ax = axes[0])
    sns.boxplot(data = df_box, x = 'month', y = 'value', ax = axes[1])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
