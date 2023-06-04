import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',
                index_col= ['date'],
                 parse_dates=['date'])


# Clean data
df = df.loc[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))
]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize= (10,5))
    sns.lineplot(data=df, c = 'r')
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    df_bar['month_number'] = df_bar.index.month

    df_bar = df_bar.groupby(['year','month']).mean().reset_index().sort_values(['month_number'])




    # Draw bar plot
    fig, ax = plt.subplots(figsize=(19, 10))
    
    sns.barplot(df_bar, x= 'year', hue='month', y='value', palette='tab10')
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.set_title("Daily freeCodeCamp Forum Average Page Views per Month")




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    from time import strptime

    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month_num'] = [strptime(x,'%b').tm_mon for x in df_box['month']]
    df_box = df_box.sort_values(['month_num'])

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(32, 10))
    
    sns.boxplot(df_box, x='month', y='value', ax = axes[1])
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    axes[1].set_title("Month-wise Box Plot (Seasonality)")

    sns.boxplot(df_box, x='year', y='value', ax = axes[0])
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    axes[0].set_title("Year-wise Box Plot (Trend)")
    



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
