import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=[0], index_col=0)

# Clean data
df = df[(df['value'].quantile(0.025) <= df['value']) &
        (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    fig = plt.figure(figsize=(20,8))
    sns.lineplot(data=df['value'])
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    fig = plt.figure(figsize=(20,8))
    sns.barplot(data=df_bar, x='year', y='value', hue='month', palette='bright', errorbar=None)
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], title="Months")
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month
    
    fig = plt.figure(figsize=(20,8))

    plt.subplot(121)
    sns.boxplot(data=df_box, x='year', y='value')
    plt.title("Year-wise Box Plot (Trend)")
    plt.xlabel('Year')
    plt.ylabel('Page Views')

    plt.subplot(122)
    df_box['month-ascii'] = df_box.index.strftime("%b")
    df_box.sort_values(by='month', inplace=True)
    sns.boxplot(data=df_box, x='month-ascii', y='value')
    plt.title("Month-wise Box Plot (Seasonality)")
    plt.xlabel('Month')
    plt.ylabel('Page Views')





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
