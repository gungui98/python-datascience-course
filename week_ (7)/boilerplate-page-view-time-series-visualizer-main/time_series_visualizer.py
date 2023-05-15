import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df['date']=pd.to_datetime(df['date'])
df = df.set_index('date')
# Clean data
df= df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    sns.lineplot(data=df, legend = False)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month
    df_bar = df_bar.groupby(['Year', 'Month'])['value'].mean().round()
    df_bar = df_bar.unstack()

    # Draw bar plot
    fig = (df_bar.plot(kind='bar', legend = True)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    legend_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',     'October', 'November', 'December']
    plt.legend(legend_labels, loc='best')




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
    df_box['monthoder'] = df_box['date'].dt.month
    df_box = df_box.sort_values('monthoder')
    fig, ax = plt.subplots(ncols = 2, figsize=(9, 4))
    ax[0] = sns.boxplot(x= df_box['year'], y= df_box['value'], ax = ax[0])
    ax[1] = sns.boxplot(x= df_box['month'], y= df_box['value'], ax = ax[1])
    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Page Views")
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Page Views")


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
