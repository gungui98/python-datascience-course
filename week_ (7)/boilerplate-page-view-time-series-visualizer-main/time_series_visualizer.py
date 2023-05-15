import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',parse_dates=[0],index_col = [0])

# Clean data
below = df.value.quantile(0.975)
under = df.value.quantile(0.025)
df = df.loc[(df.value>=under) & (df.value <= below)]
def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize = (20,8))
    sns.lineplot(df.value, c = 'r')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    # Draw bar plot
    fig = plt.figure(figsize=(10,15))
    
    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month_name()
    df_bar['month_num'] = df_bar.index.month
    df_bar = df_bar.groupby(['Year','Month']).mean().reset_index().sort_values(['month_num'])
    df_bar.rename(columns={'Year':'Years','value':'Average Page Views'},inplace=True)
    sns.barplot(data = df_bar,x = 'Years',hue = 'Month', y = 'Average Page Views')
    plt.title('Months')
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)

    # Draw box plots (using Seaborn)
    df_bar = df.copy()
    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month_name()
    df_bar['month_num'] = df_bar.index.month
    df_bar.sort_values(['month_num'],inplace=True)
    fig, axes = plt.subplots(1,2,figsize=(20,6))
    sns.boxplot(data = df_bar,x = 'Year',y = 'value',ax = axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(data = df_bar,x = 'Month',y = 'value',ax = axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_ylabel('Page Views')
    axes[1].set_xticklabels(labels = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],rotation = 45,ha = 'center') 

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
