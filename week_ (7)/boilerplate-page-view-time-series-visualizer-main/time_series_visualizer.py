import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col = 0, parse_dates = True)

# Clean data
df = df[(df.value >= df.value.quantile(0.025)) & (df.value <= df.value.quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize = (14, 6))
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    sns.lineplot(df, legend = False)
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Years'] = df_bar.index.year
    df_bar['Months'] = df_bar.index.month
    df_bar = df_bar.groupby(['Years', 'Months']).mean().reset_index()
    df_bar = df_bar.sort_values(['Years', 'Months'])
    # Draw bar plot
    fig, ax = plt.subplots(figsize = (14, 6))
    sns.barplot(df_bar, x = 'Years', y = 'value', hue = 'Months')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles , month, loc = 'upper left', title = 'Months')
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
    fig, ax = plt.subplots(1, 2, figsize = (14, 6))
    sns.boxplot(df_box, x = 'year', y = 'value', ax = ax[0])
    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Page Views")
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(data=df_box, x="month", y="value", order=month_order, ax=ax[1])
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Page Views")




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
