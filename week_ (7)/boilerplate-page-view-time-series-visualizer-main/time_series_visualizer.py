import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates = [0], index_col = 0)

# Clean data
low = df['value'].quantile(0.025)
high = df['value'].quantile(0.925)
df = df[(df['value'] <= high) & (df['value'] >= low)]


def draw_line_plot():
    # Draw line plot
	fig, ax = plt.subplots(figsize = (32, 10))
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.plot(df, color = 'red');




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Years'] = df.index.year
    df_bar['Months'] = df.index.month_name()
    df_bar = df_bar.groupby(['Years', 'Months'], sort = False)['value'].mean().round().astype(int).to_frame()
    df_bar = df_bar.rename(columns = {'value' : 'Average Page Views'})
    df_bar = df_bar.reset_index()
    missing_data = {'Years' : [2016, 2016, 2016, 2016],
                    'Months' : ['January', 'February', 'March', 'April'],
                    'Average Page Views' : [0, 0, 0, 0]}

    df_bar = pd.concat([pd.DataFrame(missing_data), df_bar])

    # Draw bar plot
	fig, ax = plt.subplots(figsize = (20, 18))
	sns.barplot(data = df_bar, x = 'Years', y = 'Average Page Views', hue = 'Months', palette = 'tab10')




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
	fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols = 2, figsize = (14, 6))

    sns.boxplot(data = df_box, x = 'year', y = 'value', ax = ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(data = df_box, x = 'month', y = 'value',order = month_order, ax = ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
